# write a python program to print duplicates in a list


l = ["hello", 10, 20, 10, 20, 10, 30, 'm', 'm']

# not allowed
text = 'hello'
# text[2]='l'
d = []

for ele in l:
    if l.count(ele) > 1 and ele not in d:
        d.append(ele)

print(d, text[1:3])
