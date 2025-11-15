# Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

x = int(input())
y = int(input())

while x < y:
    print(x, end=' ')
    x += 5

if x == y:
    print(x, end=' ')

else:

    print("Second integer can\'t be less than the first", end='')
