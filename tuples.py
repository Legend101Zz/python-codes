# write a python program to convert a tuple to a string

a = ('a', 'b', 'c', 'd')
l = ''

for ele in a:
    l = l+ele

print(l)

# other method

my_tuple = (1, 2, 3, 4, 5)

tuple_as_string = ''.join(map(str, my_tuple))

print(tuple_as_string)
