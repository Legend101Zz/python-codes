n = int(input("enter the number of rows:"))

# floyd Triangle
num = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(num, end="")
        num = num + 1
    print()


# string triangle

string = input("enter the string")
length = len(string)

for row in range(length):
    for col in range(row+1):
        print(string[col], end="")

    print()
