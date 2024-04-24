# S1 solved

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
apart = []

pos_x = [-1,1,0,0]
pos_y = [0,0,-1,1]

def find_apart(x, y):
    q = deque()
    q.append((x, y))

    visit[x][y] = True
    apart_size = 1
    while q:
        cx, cy = q.popleft()
        for pos in range(4):
            nx = cx + pos_x[pos]
            ny = cy + pos_y[pos]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '1' and visit[nx][ny] == False:
                visit[nx][ny] = True
                apart_size += 1
                q.append((nx, ny))
    apart.append(apart_size)


for i in range(N):
    for j in range(N):
        if visit[i][j] == False and board[i][j] == '1':
            find_apart(i, j)

apart.sort()
print(len(apart))
for i in apart:
    print(i)