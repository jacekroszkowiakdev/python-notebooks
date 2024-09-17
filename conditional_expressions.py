# conditional expressions: one-liner shorthand for if-else statement (ternary operator)
# print or assign one of two values following the formula: X if condition evaluates to true, else return Y

num = int(input(f"pick an integer: "))

a = 6
b = 7

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"

print(result)

