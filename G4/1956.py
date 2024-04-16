# G4 solved
# [단기간 성장](https://www.acmicpc.net/workbook/view/4349)

import sys
from math import inf
input = sys.stdin.readline

V, E = map(int, input().split())

board = [[inf for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    # a -> b 거리 c
    a, b, c = map(int, input().split())
    board[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

min_cycle = inf
for i in range(V+1):
    min_cycle = min(min_cycle, board[i][i])

if min_cycle == inf:
    print(-1)
else:
    print(min_cycle)