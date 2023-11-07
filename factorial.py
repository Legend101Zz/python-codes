# built-in
import math
n = int(input("enter the number of rows:"))
result = math.factorial(n)
print(result)


# by recursion

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# by Loops


result = 1

for i in range(n, 0, -1):
    result = result*i

print(result)
