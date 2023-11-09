# write a python program to print duplicates in a list


import random
l = ["hello", 10, 20, 10, 20, 10, 30, 'm', 'm']
m = ['1', '2', '3']
# not allowed
text = 'hello'
# text[2]='l'
d = []

for ele in l:
    if l.count(ele) > 1 and ele not in d:
        d.append(ele)

new_list = [x for (i, x) in enumerate(l) if i not in (0, 3, 5)]
random.shuffle(m)
print(d, text[1:3], new_list, m)
