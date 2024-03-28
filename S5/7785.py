# S5

import sys
input = sys.stdin.readline

n = int(input())
enter = {}
for i in range(n):
    name, ent = input().strip().split()
    if ent == "enter":
        enter[name] = True
    else:
        del enter[name]

print("\n".join(sorted(enter.keys(), reverse = True)))