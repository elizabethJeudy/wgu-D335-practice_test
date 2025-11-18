# Create a solution that accepts an integer input representing
# any number of ounces. Output the converted total number of
# tons, pounds, and remaining ounces based on the value of the
# input ounces. There are 16 ounces in a pound and 2,000 pounds
# in a ton.
# The solution output should be in the format:
# Tons: value_1
# Pounds: value_2
# Ounces: value_3

print("Enter the number of ounces to convert:")
ounces = int(input())


# with provided info, we know there are 2000 pounds in a ton
# and 16 ounces in a pound
# to find how many ounces are in a ton we multiple 2000 * 16 + 32000 ounces

tons = ounces // 32000  # returns whole int of tons
# calculate how many ounces are remaining for pounds
remaining_ounces = ounces % 32000
pounds = remaining_ounces // 16  # returns whole int of pounds remaining
# calculate remaining ounces
remaining_ounces %= 16

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {remaining_ounces}")
