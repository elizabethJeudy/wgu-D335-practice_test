# Given three input values representing counts of nickels, dimes, and quarters, output the total amount as dollars and cents.
# Output each floating-point value with two digits after the decimal point using the following statement:


nickels_count = float(input())
dimes_count = float(input())
quarters_count = float(input())

nickels = nickels_count * 0.05
dimes = dimes_count * 0.10
quarters = quarters_count * 0.25

dollars = nickels + dimes + quarters

print(f"Amount: ${dollars:.2f}")
