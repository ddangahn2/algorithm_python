# S1 solved

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(M)]

visited = [[False for _ in range(N)] for _ in range(M)]
x = [-1,1,0,0]
y = [0,0,-1,1]

W = 0
B = 0

def bfs(i, j):
    flag = board[i][j]
    visited[i][j] = True
    count = 1

    q = deque()
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for dir in range(4):
            ni = ci + x[dir]
            nj = cj + y[dir]
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and board[ni][nj] == flag:
                visited[ni][nj] = True
                q.append((ni, nj))
                count += 1
    
    return flag, count ** 2


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            flag, power = bfs(i, j)
            if flag == "W":
                W += power
            else:
                B += power

print(W, B)