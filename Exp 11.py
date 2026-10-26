grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["mouse"]],
    "V": [["chased"], ["saw"]]
}
def parse(symbols, words):
    if not symbols:
        return len(words) == 0
    first = symbols[0]
    remaining = symbols[1:]
    if first not in grammar:
        if words and first == words[0]:
            return parse(remaining, words[1:])
        return False
    for production in grammar[first]:
        if parse(production + remaining, words):
            return True
    return False
while True:
    sentence = input("\nEnter a sentence (or 'exit' to stop): ").lower()
    if sentence == "exit":
        print("Program terminated.")
        break
    words = sentence.split()
    if parse(["S"], words):
        print("Sentence is grammatically valid.")
    else:
        print("Sentence is grammatically invalid.")
