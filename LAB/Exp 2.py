def check_string(s):
    state = 0
    for ch in s:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if ch == 'a':
                state = 1
            elif ch == 'b':
                state = 2
        elif state == 2:
            if ch == 'a':
                state = 1
            elif ch == 'b':
                state = 0
    return state == 2
s = input("Enter a string containing a and b: ")
if check_string(s):
    print("String accepted")
else:
    print("String rejected")
