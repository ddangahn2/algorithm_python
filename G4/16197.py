# G4 solved


import sys
from collections import deque
input = sys.stdin.readline

# 세로, 가로
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

coin = []

for i in range(N):
    for j in range(M):
        if board[i][j] == "o":
            coin.append([i, j])

visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

x = [-1,1,0,0]
y = [0,0,-1,1]

def bfs():
    q = deque()
    q.append([coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0])
    visited[coin[0][0]][coin[0][1]][coin[1][0]][coin[1][1]] = True
    
    while q:
        coin1_x, coin1_y, coin2_x, coin2_y, count = q.popleft()

        if count >= 10:
            return -1
        
        for dir in range(4):
            new_coin1_x = coin1_x + x[dir]
            new_coin2_x = coin2_x + x[dir]
            new_coin1_y = coin1_y + y[dir]
            new_coin2_y = coin2_y + y[dir]
            if 0 <= new_coin1_x < N and 0 <= new_coin1_y < M and 0 <= new_coin2_x < N and 0 <= new_coin2_y < M:
                if board[new_coin1_x][new_coin1_y] == "#":
                    new_coin1_x -= x[dir]
                    new_coin1_y -= y[dir]
                if board[new_coin2_x][new_coin2_y] == "#":
                    new_coin2_x -= x[dir]
                    new_coin2_y -= y[dir]
                if new_coin1_x == new_coin2_x and new_coin1_y == new_coin2_y:
                    continue
                if not visited[new_coin1_x][new_coin1_y][new_coin2_x][new_coin2_y]:
                    visited[new_coin1_x][new_coin1_y][new_coin2_x][new_coin2_y] = True
                    q.append([new_coin1_x, new_coin1_y, new_coin2_x, new_coin2_y, count + 1])
            elif 0 <= new_coin1_x < N and 0 <= new_coin1_y < M:
                return count + 1
            elif 0 <= new_coin2_x < N and 0 <= new_coin2_y < M:
                return count + 1
    return -1
                
print(bfs())