# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.

# The solution output should be in the format:

# xxx-xx-xxxx

student_id = int(input("Enter Student Identification Number: \n"))

# to format id we need to:
# 1. convert integer to string str(student_id)
# 2. find how many number are in the string len(str(student_id))
# 3. calculate zeros needed to make it 9 digits (9 - len(str(student_id)))

format_id = ("0" * (9 - len(str(student_id))) + str(student_id))

# grab character from needed positions and add the dashes
print(format_id[0:3] + "-" + format_id[3:5] + "-" + format_id[5:9])
