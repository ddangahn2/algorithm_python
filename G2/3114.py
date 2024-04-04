# G2 solved

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip().split()) for _ in range(R)]
apple = [[0 for _ in range(C)] for _ in range(R)]
banana = [[0 for _ in range(C)] for _ in range(R)]

# 0 0 1 1    2 2 2 1
# 0 1 1 1 -> 3 3 2 1
# 0 0 0 0    0 0 0 0

for i in range(R):
    add = 0
    for j in reversed(range(C)):
        # <- 방향으로 더해서 넣어야함
        if board[i][j][0] == "B":
            add += int(board[i][j][1:])
        banana[i][j] = add

for i in range(C):
    add = 0
    for j in reversed(range(R)):
        # ⭡ 방향으로 더해서 넣어야함
        if board[j][i][0] == "A":
            add += int(board[j][i][1:])
        apple[j][i] = add

fruit = [[0 for _ in range(C)] for _ in range(R)]

for i in reversed(range(R-1)):
    for j in reversed(range(C-1)):
        fruit[i][j] = max(fruit[i][j+1] + apple[i+1][j], fruit[i+1][j] + banana[i][j+1], fruit[i+1][j+1] + apple[i+1][j] + banana[i][j+1])

print(fruit[0][0])