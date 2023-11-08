# write a python program to convert a tuple to a string

a = ('a', 'b', 'c', 'd', 'a')
l = ''

for ele in a:
    l = l+ele

print(l)

# other method

my_tuple = (1, 2, 3, 4, 5)

tuple_as_string = ''.join(map(str, my_tuple))

print(tuple_as_string)


# Write a python program to get the 4th element and 4th element from the last of a tuple

def get_fourth_index(tuple_1):
    return tuple_1[3], tuple_1[-4]


# write a python program to find repeadted items of a tuple

def find_repeated(tuple):
    result = []
    for ele in tuple:
        if tuple.count(ele) > 1 and ele not in result:
            result.append(ele)
    return print(result)


find_repeated((1, 2, 3, 4, 4, 5, 5, 5))


# to find if a element exits ina tuple or not

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Element to check for existence
element_to_find = 3

# Check if the element exists in the tuple
if element_to_find in my_tuple:
    print(f"{element_to_find} exists in the tuple.")
else:
    print(f"{element_to_find} does not exist in the tuple.")
