import re
text = input("Enter a text: ")
pattern = input("Enter a pattern to search: ")
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")
