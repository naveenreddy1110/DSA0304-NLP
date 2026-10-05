import re

text = "The quick brown fox jumps over the lazy dog. Contact us at info@example.com or support@company.org."

print("=== Original Text ===")
print(text)
print("\n")

print("--- 1. re.search() Examples ---")
fox_match = re.search(r'fox', text)
if fox_match:
    print(f"Found 'fox' at position: {fox_match.span()}") 
else:
    print("'fox' not found.")

cat_match = re.search(r'cat', text)
if cat_match:
    print(f"Found 'cat' at position: {cat_match.span()}")
else:
    print("'cat' not found.")
print("\n")

print("--- 2. re.findall() Examples ---")
short_words = re.findall(r'\b[a-z]{3,5}\b', text)
print(f"Words of 3 to 5 letters: {short_words}")

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print(f"Extracted emails: {emails}")
print("\n")

print("--- 3. re.match() Examples ---")
start_match = re.match(r'The', text)
print(f"Match at start ('The'): {'Success' if start_match else 'Failed'}")

quick_match = re.match(r'quick', text)
print(f"Match at start ('quick'): {'Success' if quick_match else 'Failed'}")
print("\n")

print("--- 4. re.sub() Example ---")
anonymized_text = re.sub(email_pattern, '[REDACTED]', text)
print(f"Anonymized Text:\n{anonymized_text}")