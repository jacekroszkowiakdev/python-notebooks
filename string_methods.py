name = input("Enter your name: ")

# String length
print(f"Your name has {len(name)} letters.")

# Find the position of the first occurrence of 'a'
if "a" in name:
    print(f"Letter 'a' is at position {name.find('a')}.")
else:
    print("Letter 'a' is not in your name.")

# Find the position of the last occurrence of 'k'
if "k" in name:
    print(f"Letter 'k' is at position {name.rfind('k')}.")
else:
    print("Letter 'k' is not in your name.")

print(name.capitalize())
print(name.upper())
print(name.lower())
# Checks if all characters in the string are digits (0-9).
print(name.isdigit())
# Checks if all characters in the string are alphabetic (A-Z, a-z).
print(name.isalpha())
# Counts the number of occurrences of the character 'a' in the string.
print(name.count('a'))