a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
m = a.keys() - b.keys()
n = a.items() & b.items()
p = [1, 2, 3, 4, 6, 7]

print(m, n, max(p))
