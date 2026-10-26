
# Parse Tree Generation using CFG

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["N"], ["Pronoun"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["mouse"], ["cricket"]],
    "V": [["chased"], ["saw"], ["like"]],
    "Pronoun": [["i"], ["you"], ["he"], ["she"], ["we"], ["they"]]
}

def parse_symbol(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return [(symbol, pos + 1)]
        return []

    results = []

    for production in grammar[symbol]:
        partials = [([], pos)]

        for item in production:
            new_partials = []

            for children, current_pos in partials:
                matches = parse_symbol(item, words, current_pos)

                for node, next_pos in matches:
                    new_partials.append(
                        (children + [node], next_pos)
                    )

            partials = new_partials

            if not partials:
                break
        for children, end_pos in partials:
            results.append(((symbol, children), end_pos))
    return results
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
    results = parse_symbol("S", words, 0)

    tree = None

    for node, end_pos in results:
        if end_pos == len(words):
            tree = node
            break

    if tree is not None:
        print("Parse tree:")
        print_tree(tree)
    else:
        print("No valid parse tree found.")
