# Create a solution that accepts three integer inputs
# representing the number of times an employee travels to
# a job site in a month. Output the total distance traveled
# to two decimal places according to the miles each employee
#  commutes to the job site:
# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles
# The solution output should be in the format:
# Distance: total_miles_traveled miles

# 3 int inputs for trips employee made
print("Enter the number of days Employee A travels to job:")
Employee_A = int(input())
print("Enter the number of days Employee B travels to job:")
Employee_B = int(input())
print("Enter the number of days Employee C travels to job:")
Employee_C = int(input())

# miles each employee travels
miles_A = 15.62
miles_B = 41.85
miles_C = 32.67

# calculate the toal distance by multiplying miles and distance, the adding all 3 together

total_distance = (Employee_A * miles_A) + \
    (Employee_B * miles_B) + (Employee_C * miles_C)

print(f'Distance: {total_distance:.2f} miles')
