# Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type before finding the sum.

# First output: the sum of the five inputs as an integer value
# Second output: the sum of the five inputs after converting each input to a float value
# Third output: the concatenation of the five inputs after converting each input to a string
# The solution output should be in the format:

# Integer: integer_sum_value
# Float: float_sum_value
# String: string_sum_value

num_1 = int(input("Enter 1st number: \n"))
num_2 = int(input("Enter 2nd number: \n"))
num_3 = int(input("Enter 3rd number: \n"))
num_4 = int(input("Enter 4th number: \n"))
num_5 = int(input("Enter 5th number: \n"))

# sum of 5 inputs as integer
integer_total = num_1 + num_2 + num_3 + num_4 + num_5
print(f"Integer: {integer_total}")

# sum of 5 inputs after converting each to float
float_total = float(num_1) + float(num_2) + \
    float(num_3) + float(num_4) + float(num_5)
print(f"Float: {float_total}")

# 5 inputs concatenated as string
string_total = str(num_1) + str(num_2) + str(num_3) + str(num_4) + str(num_5)
print(f"String: {string_total}")
