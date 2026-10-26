grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["mouse"]],
    "V": [["chased"], ["saw"]]
}
def earley_parser(words):
    n = len(words)
    chart = [set() for _ in range(n + 1)]
    chart[0].add(("START", ("S",), 0, 0))
    for i in range(n + 1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):
                lhs, rhs, dot, start = state
                if dot < len(rhs):
                    symbol = rhs[dot]
                    if symbol in grammar:
                        for production in grammar[symbol]:
                            new_state = (
                                symbol, tuple(production), 0, i
                            )
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True
                    elif i < n and words[i] == symbol:
                        new_state = (lhs, rhs, dot + 1, start)
                        chart[i + 1].add(new_state)
                else:
                    for prev in list(chart[start]):
                        plhs, prhs, pdot, pstart = prev

                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (
                                plhs, prhs, pdot + 1, pstart
                            )
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True
    return ("START", ("S",), 1, 0) in chart[n]
while True:
    sentence = input(
        "\nEnter a sentence (or 'exit' to stop): "
    ).lower().strip()

    if sentence == "exit":
        print("Program terminated.")
        break

    words = sentence.split()

    if earley_parser(words):
        print("Sentence is grammatically valid.")
    else:
        print("Sentence is grammatically invalid.")
