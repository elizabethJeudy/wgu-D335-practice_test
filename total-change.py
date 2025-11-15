# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

change = int(input())

dollar = change // 100
change %= 100
quarter = change // 25
change %= 25
dime = change // 10
change %= 10
nickel = change // 5
change %= 5
penny = change // 1
change %= 1

# build parts and print them on a single line separated by spaces
parts = []

if dollar > 0:
    parts.append("1 Dollar" if dollar == 1 else f"{dollar} Dollars")

if quarter > 0:
    parts.append("1 Quarter" if quarter == 1 else f"{quarter} Quarters")

if dime > 0:
    parts.append("1 Dime" if dime == 1 else f"{dime} Dimes")

if nickel > 0:
    parts.append("1 Nickel" if nickel == 1 else f"{nickel} Nickels")

if penny > 0:
    parts.append("1 Penny" if penny == 1 else f"{penny} Pennies")

if parts:
    print(" ".join(parts))
else:
    print("No change")
