n = int(input("enter the number of rows:"))
# pattern 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# pattern 2

for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()
