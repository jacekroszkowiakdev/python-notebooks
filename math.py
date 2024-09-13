# arithmetic operators

# addition
money = 1
money = money + 1
money += 1

# substraction
money = money - 1
money -= 1

# multiplication

money = money * 4
money *= 2

# division
money = money / 2
money /= 2

# exponentiation (Alternative to pow() function)
money = money ** 2
money **= 2

# modulus - gives the remainder to any division
remainder = money % 2 #this finds if number is odd or even

print(remainder)

# operations
# build in functions, not methods (methods are usually tied to objects).

x = 3.14
y = 4
z = 5

 # Rounds a floating-point number to the nearest integer
print(round(x))

# Returns the absolute value of a number, which is its distance from zero (i.e., it converts negative numbers to positive, and positive numbers remain unchanged).
print(abs(y))

#Returns the value of base raised to the power of exp. It's equivalent to the ** operator but is written as a function.
print(pow(4, 3))

# Returns the largest value from the provided arguments.
print(max(x, y, z))

# Returns the smallest value from the provided arguments.
print(min(x, y, z))