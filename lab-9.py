# Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:

# If the temperature is below 33° F, the water is “Frozen”.
# If the water is between 33° F and 80° F(including 33°), the water is “Cold”.
# If the water is between 80° F and 115° F(including 80°), the water is "Warm".
# If the water is between 115° F and 211° F(including 115°), the water is “Hot".
# If the water is greater than or equal to 212° F, the water is “Boiling”.
# Additionally, output a safety comment only during the following circumstances:

# If the water is exactly 212° F, the safety comment is, "Caution: Hot!"
# If the water temperature is less than 33° F, the safety comment is, "Watch out for ice!"
# The solution output should be in the format:

# water_state
# optional_safety_comment


water_temp = int(input("Enter the water temperature:\n"))

if water_temp < 33:
    print("Frozen")
    print("Watch out for the ice!")
elif 33 <= water_temp < 80:
    print("Cold")
elif 80 <= water_temp < 155:
    print("Warm")
elif 155 <= water_temp < 211:
    print("Hot")
else:
    print("Boiling")
    if water_temp == 212:
        print("Caution: Hot!")
