# S1 solved
# [대기업 코테에서 나오는 유형 모음](https://www.acmicpc.net/workbook/view/8708)

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dist_board = [[-1 for _ in range(M)] for _ in range(N)]

st_x = 0
st_y = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            st_x = i
            st_y = j

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
def bfs():
    dist_board[st_x][st_y] = 0

    q = deque()
    q.append((st_x, st_y))

    while q:
        cx, cy = q.popleft()

        for dir in range(4):
            nx = cx + x[dir]
            ny = cy + y[dir]
            if 0 <= nx < N and 0 <= ny < M and dist_board[nx][ny] == -1 and board[nx][ny] != 0:
                dist_board[nx][ny] = dist_board[cx][cy] + 1
                q.append((nx, ny))

bfs()

for i in range(N):
    for j in range(M):
        if dist_board[i][j] == -1 and board[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist_board[i][j], end=' ')
    print()