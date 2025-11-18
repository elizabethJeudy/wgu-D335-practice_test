# Create a solution that accepts any three
# integer inputs representing the base
# (b1, b2) and height (h) measurements of a trapezoid in meters.
# Output the exact area of the trapezoid in square meters as a float value.
# The exact area of a trapezoid can be calculated by summing the two bases, multiplying
# the sum by the height, and then dividing by two.

# Trapezoid Area Formula:
# A = ((b1 + b2) * h) / 2

# The solution output should be in the format:

# Trapezoid area: area_value square meters

b1 = int(input("Enter base 1: \n"))
b2 = int(input("Enter base 2: \n"))
height = int(input("Enter height: \n"))

trapezoid_area = ((b1 + b2) * height) / 2

print(f"Trapezoid area: {trapezoid_area} square meters")
