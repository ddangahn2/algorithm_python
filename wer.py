a = {1:2, 3:1, 2:1}

print(list(a.items()))

print(sorted(list(a.items()), key=lambda x: (x[1], x[0])))