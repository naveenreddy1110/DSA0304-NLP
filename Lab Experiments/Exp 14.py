grammar = {
    "S": [["NP_S", "VP_S"], ["NP_P", "VP_P"]],

    "NP_S": [["Det", "N_S"], ["N_S"], ["Pronoun_S"]],
    "NP_P": [["Det", "N_P"], ["N_P"], ["Pronoun_P"]],

    "VP_S": [["V_S"], ["V_S", "NP_O"]],
    "VP_P": [["V_P"], ["V_P", "NP_O"]],

    "NP_O": [["Det", "N_O"], ["N_O"]],

    "Det": [["the"], ["a"]],

    "N_S": [
        ["boy"], ["girl"], ["cat"], ["dog"],
        ["student"], ["teacher"], ["mouse"]
    ],

    "N_P": [
        ["boys"], ["girls"], ["cats"], ["dogs"],
        ["students"], ["teachers"], ["mice"]
    ],

    "Pronoun_S": [["he"], ["she"], ["it"]],
    "Pronoun_P": [["they"], ["we"], ["you"]],

    "V_S": [
        ["runs"], ["likes"], ["plays"], ["chases"]
    ],

    "V_P": [
        ["run"], ["like"], ["play"], ["chase"]
    ],

    "N_O": [
        ["boy"], ["girl"], ["cat"], ["dog"],
        ["student"], ["teacher"], ["mouse"],
        ["boys"], ["girls"], ["cats"], ["dogs"],
        ["students"], ["teachers"], ["mice"],
        ["cricket"], ["football"], ["book"]
    ]
}


def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return [pos + 1]
        return []

    results = []

    for production in grammar[symbol]:
        positions = [pos]

        for item in production:
            next_positions = []

            for current_pos in positions:
                next_positions.extend(
                    parse(item, words, current_pos)
                )

            positions = next_positions

            if not positions:
                break

        results.extend(positions)

    return results


while True:
    sentence = input(
        "\nEnter a sentence (or 'exit' to stop): "
    ).lower().strip()

    if sentence == "exit":
        print("Program terminated.")
        break

    words = sentence.split()

    if words and len(words) in parse("S", words, 0):
        print("Subject-verb agreement is correct.")
    else:
        print("Invalid sentence or subject-verb disagreement.")
