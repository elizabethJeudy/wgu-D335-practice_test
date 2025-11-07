# Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.
# Output each floating-point value with two digits after the decimal point

# steps: divide given miles by gas mileage to return gallons; multiply gallons used by gas cost


gas_mileage = float(input())
gas_cost = float(input())

mileage_20 = 20 / gas_mileage * gas_cost
mileage_75 = 75 / gas_mileage * gas_cost
mileage_500 = 500 / gas_mileage * gas_cost

print(f'{mileage_20:.2f} {mileage_75:.2f} {mileage_500:.2f}')
