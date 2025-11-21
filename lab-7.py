# Create a program that takes an integer input and determines whether it equals one of the values in this predefined list:

# predef_list = [4, -27, 15, 33, -10]

# Define a function named is_in_list() that outputs a Boolean value(True or False) based on whether the input value is present in predef_list.

# The solution should produce the output in the following format:

# True if the input is in the list, otherwise False.

predef_list = [4, -27, 15, 33, -10]

# grabs user input
user_input = int(input("Enter the number to check for in the list:\n"))

# function checks arguments (user input to predefined list) and returns true or false


def is_in_list(predef_list, user_input):
    if user_input in predef_list:
        print("Is the input present in the list?", end=' ')
        return True
    else:
        print("Is the input present in the list?", end=' ')
        return False


if __name__ == '__main__':
    print(is_in_list(predef_list, user_input))
