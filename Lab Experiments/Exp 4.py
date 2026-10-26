def make_plural(word):
    if word.endswith(("s", "x", "z", "ch", "sh")):
        plural = word + "es"
    elif word.endswith("y") and word[-2].lower() not in "aeiou":
        plural = word[:-1] + "ies"
    else:
        plural = word + "s"
    return plural
word = input("Enter a singular noun: ")
print("Plural form:", make_plural(word))
