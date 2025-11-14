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

# checks if there is any change
if dollar == 0 and quarter == 0 and dime == 0 and nickel == 0 and penny == 0:
    print("No change")


if dollar > 0:
    if dollar == 1:
        print("1 Dollar")  # singular
    else:
        print(f'{dollar} Dollars')  # plural


if quarter > 0:
    if quarter == 1:
        print("1 Quarter")
    else:
        print(f'{quarter} Quarters')

if dime > 0:
    if dime == 1:
        print("1 Dime")
    else:
        print(f'{dime} Dimes')

if nickel > 0:
    if nickel == 1:
        print("1 Nickel")
    else:
        print(f'{nickel} Nickels')

if penny > 0:
    if penny == 1:
        print('1 Penny')
    else:
        print(f'{penny} Pennies')
