print("Type 2 numbers")

a = int(input())
b = int(input())

print("If you want to add, type 1. If you want to subtract, type 2")

x = int(input())

if x == 1:
    print(a + b)
elif x == 2:
    print(a - b)
