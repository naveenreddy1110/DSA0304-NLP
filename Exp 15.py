
# Probabilistic Context-Free Grammar (PCFG) Parser

from functools import lru_cache

grammar = {
    "S": [(1.0, ("NP", "VP"))],

    "NP": [
        (0.7, ("Det", "N")),
        (0.2, ("Pronoun",)),
        (0.1, ("N",))
    ],

    "VP": [(1.0, ("V", "NP"))],

    "Det": [
        (0.6, ("the",)),
        (0.4, ("a",))
    ],

    "N": [
        (0.2, ("cat",)),
        (0.2, ("dog",)),
        (0.2, ("mouse",)),
        (0.2, ("cricket",)),
        (0.2, ("book",))
    ],

    "V": [
        (0.5, ("chased",)),
        (0.25, ("saw",)),
        (0.25, ("like",))
    ],

    "Pronoun": [
        (0.2, ("i",)),
        (0.2, ("you",)),
        (0.2, ("he",)),
        (0.2, ("she",)),
        (0.2, ("they",))
    ]
}


def pcfg_parse(words):
    @lru_cache(maxsize=None)
    def parse_symbol(symbol, start, end):
        # Match a terminal word
        if symbol not in grammar:
            if end == start + 1 and words[start] == symbol:
                return 1.0, symbol
            return None

        best = None

        # Try every production for this symbol
        for rule_probability, production in grammar[symbol]:
            result = parse_sequence(production, start, end)

            if result is not None:
                sequence_probability, children = result
                probability = (
                    rule_probability * sequence_probability
                )

                if best is None or probability > best[0]:
                    best = (
                        probability,
                        (symbol, children)
                    )

        return best

    @lru_cache(maxsize=None)
    def parse_sequence(symbols, start, end):
        if not symbols:
            if start == end:
                return 1.0, ()
            return None

        best = None
        first = symbols[0]
        remaining = symbols[1:]

        for split in range(start + 1, end + 1):
            first_result = parse_symbol(first, start, split)

            if first_result is None:
                continue

            rest_result = parse_sequence(remaining, split, end)

            if rest_result is None:
                continue

            probability = first_result[0] * rest_result[0]
            children = (first_result[1],) + rest_result[1]

            if best is None or probability > best[0]:
                best = (probability, children)

        return best

    return parse_symbol("S", 0, len(words))


def print_tree(tree, level=0):
    if isinstance(tree, str):
        print("  " * level + tree)
    else:
        print("  " * level + tree[0])

        for child in tree[1]:
            print_tree(child, level + 1)


while True:
    sentence = input(
        "\nEnter a sentence (or 'exit' to stop): "
    ).lower().strip()

    if sentence == "exit":
        print("Program terminated.")
        break

    words = sentence.split()

    result = pcfg_parse(words)

    if result is not None:
        probability, tree = result

        print("Sentence parsed successfully.")
        print("Most probable parse tree:")
        print_tree(tree)
        print("Parse probability:", round(probability, 6))
    else:
        print("Sentence cannot be parsed using this grammar.")
