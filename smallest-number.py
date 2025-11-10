# write program whose inputs aare 3 integers and output is the smallest value

x = int(input())
y = int(input())
z = int(input())

smallest = x

if y < smallest:
    smallest = y
    if z < smallest:
        smallest = z
elif z < smallest:
    smallest = z

print(f"The smallest value is {smallest}")
