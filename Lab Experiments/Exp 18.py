
# Simple FOPC Parser using Python

import re


def tokenize(expression):
    pattern = re.compile(
        r"\s*(<->|->|[∀∃¬∧∨→↔~!&|(),.=]|[A-Za-z_][A-Za-z0-9_]*)"
    )

    tokens = []
    position = 0

    aliases = {
        "forall": "∀",
        "exists": "∃",
        "not": "¬",
        "and": "∧",
        "or": "∨",
        "implies": "→",
        "iff": "↔",
        "~": "¬",
        "!": "¬",
        "&": "∧",
        "|": "∨",
        "->": "→",
        "<->": "↔"
    }

    while position < len(expression):
        if not expression[position:].strip():
            break

        match = pattern.match(expression, position)

        if not match:
            raise ValueError(
                "Invalid character: " + expression[position]
            )

        token = match.group(1)
        token = aliases.get(token.lower(), aliases.get(token, token))

        tokens.append(token)
        position = match.end()

    return tokens


class FOPCParser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def accept(self, token):
        if self.current() == token:
            self.pos += 1
            return True
        return False

    def expect(self, token):
        if not self.accept(token):
            raise ValueError("Expected '" + token + "'")

    def expect_identifier(self):
        token = self.current()

        if token is not None and re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*", token
        ):
            self.pos += 1
            return token

        raise ValueError("Expected an identifier")

    def parse(self):
        if not self.tokens:
            raise ValueError("Expression is empty")

        result = self.parse_iff()

        if self.current() is not None:
            raise ValueError("Unexpected token: " + self.current())

        return result

    def parse_iff(self):
        node = self.parse_imp()

        while self.accept("↔"):
            right = self.parse_imp()
            node = ("IFF", node, right)

        return node

    def parse_imp(self):
        left = self.parse_or()

        if self.accept("→"):
            right = self.parse_imp()
            return ("IMPLIES", left, right)

        return left

    def parse_or(self):
        node = self.parse_and()

        while self.accept("∨"):
            right = self.parse_and()
            node = ("OR", node, right)

        return node

    def parse_and(self):
        node = self.parse_unary()

        while self.accept("∧"):
            right = self.parse_unary()
            node = ("AND", node, right)

        return node

    def parse_unary(self):
        if self.accept("¬"):
            return ("NOT", self.parse_unary())

        if self.current() in ("∀", "∃"):
            quantifier = self.current()
            self.pos += 1

            variable = self.expect_identifier()
            body = self.parse_unary()

            return (quantifier, variable, body)

        return self.parse_atom()

    def parse_atom(self):
        if self.accept("("):
            node = self.parse_iff()
            self.expect(")")
            return node

        name = self.expect_identifier()

        if self.accept("="):
            value = self.expect_identifier()
            return ("EQUALS", name, value)

        if self.accept("("):
            arguments = []

            if self.current() != ")":
                arguments.append(self.expect_identifier())

                while self.accept(","):
                    arguments.append(self.expect_identifier())

            self.expect(")")
            return ("PREDICATE", name, arguments)

        return ("ATOM", name)


while True:
    expression = input(
        "\nEnter a logical expression (or 'exit' to stop): "
    ).strip()

    if expression.lower() == "exit":
        print("Program terminated.")
        break

    try:
        tokens = tokenize(expression)
        parser = FOPCParser(tokens)
        parser.parse()

        print("Valid FOPC expression.")

    except ValueError as error:
        print("Invalid FOPC expression.")
        print("Reason:", error)
