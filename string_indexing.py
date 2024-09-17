# indexing = accessing elements of the sequence using [] and (indexing operator)
# [start: end: step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[10:14])
print(credit_number[10:])
print(credit_number[-1])

# with step
print(credit_number[::3])
print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# reverse string with step
print(credit_number[::-1])