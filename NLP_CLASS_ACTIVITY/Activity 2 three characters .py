strings = ["acb", "aacb", "abc", "acba", "bacb", "ac"]
for string in strings:
    state = "q0"
    for ch in string:
        if state == "q0":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"
        elif state == "q1":
            if ch == "c":
                state = "q2"
            else:
                state = "q1" if ch == "a" else "q0"
        elif state == "q2":
            if ch == "b":
                state = "q3"
            else:
                state = "q0"
        elif state == "q3":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"
    if state == "q3":
        print(string, "True")
    else:
        print(string, "False")
