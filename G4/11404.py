# G4 solved

import sys
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[inf for _ in range(n)] for _ in range(n)]
# bus_ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    bus[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a-1][b-1] = min(bus[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if bus[i][j] > bus[i][k] + bus[k][j]:
                bus[i][j] = bus[i][k] + bus[k][j]

for i in bus:
    for j in i:
        if j == inf:
            j = 0
        print(j, end=' ')
    print()