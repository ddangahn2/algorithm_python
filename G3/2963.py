# G3 solved

search = input()

node = 1
nodes = 1

for i in search:
    if i == 'P':
        continue
    elif i == 'L':
        node *= 2
    elif i == 'R':
        node *= 2
        node += nodes
    elif i == '*':
        node *= 5
        node += nodes
        nodes *= 3

print(node)