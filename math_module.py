import math

# The math module in Python provides access to various mathematical functions and constants. It includes functions for trigonometry, logarithms, powers, and other advanced math operations. Here's an overview of some of the key functions and constants available in the math module:

# Common Constants
# math.pi: The mathematical constant π (Pi), approximately equal to 3.14159.
# math.e: The mathematical constant e, the base of the natural logarithm, approximately equal to 2.71828.

print(math.pi)
print(math.e)

x = 9.2

print(math.sqrt(x)) # √ square root of x
print(math.ceil(x)) # rounds the float up
print(math.floor(x)) # rounds the float down


# Exercises
radius = float(input("Enter the radius fo a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference of the circle is: {round(circumference, 4)} cm")
print(f"The area of the circle is: {round(area, 4)} cm^2")

