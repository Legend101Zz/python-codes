#L shaped
n = int(input("enter the number of rows:"))

for row in range(n):
    for col in range(n):
        if col == 0 or row == n-1 or row == col:
            print('*', end="")
        else:
            print(end=" ")
    print()   


#inverse L shaped 

for row in range(0,n):
    for col in range(0,n):
        if row == 0 or col == n-1 or row == col:
            print('*', end="")
        else:
            print(end=" ")
    print()   
