# S1 solved

import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

board = [[0 for _ in range(N)] for _ in range(M)]
square = [list(map(int, input().split())) for _ in range(K)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = 1
                count += 1
    return count
# x1, y1, x2, y2에서 x2, y2 1씩 빼주기
for x1, y1, x2, y2 in square:
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = -1

area = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            area.append(bfs(i, j))
print(len(area))

for i in sorted(area):
    print(i, end=' ')