# Create a solution that accepts an integer input representing the
# index value for any of the seven elements in the following list:

# data_mixture = ["Python is fun", 2024, 5.67, [
#  "apple", "banana", "coconut"], None, {"name": "John", "age": 25}]


# The solution should perform the following:

# Retrieve the element at the given index.
# Determine its data type using the type() function and its .name attribute.
# Check if the element belongs to one of the following categories:
# If the element is "iterable" (e.g., list, str, dict), output, "This element is iterable."
# If the element is numeric(e.g., int, float), output, "This element is numeric."
# For other data types not in these categories, output, "This is a different data type."
# The solution output should be in the format:

# Element: [element_value], Type: [data_type], Message: [category_message]

data_mixture = ["Python is fun", 2024, 5.67, [
    "apple", "banana", "coconut"], None, {"name": "John", "age": 25}]

index = int(input("Enter index:\n"))

# grabs the element from list based off input
element = data_mixture[index]

# use type conversion to get data type since all differ
# __name__ grabs just the name of data type and not entire class object
data_type = type(element).__name__

# isinstance checks if provided elements are any of the types listed

if isinstance(element, (list, str, dict)):
    message = "This element is iterable."

elif isinstance(element, (int, float)):
    message = "This element is numeric."

else:
    message = "This is a different data type."


print(f"Element: {element}, Type: {data_type}, Message: {message}")
