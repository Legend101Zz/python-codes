# number of n digits which are equal to sum of nth power of its digits eg: 0-9 ,153 ( 1^3 + 5^3 + 3^3 = 153)


for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while (i != 0):
        digit = i % 10
        result = result + digit**n
        i = i//10
    if (num == result):
        print(num)
