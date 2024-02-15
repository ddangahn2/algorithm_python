# G4 solved

import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().strip()) for _ in range(R)]
alpha = set()

x = [-1,1,0,0]
y = [0,0,-1,1]

alpha.add(board[0][0])

gmax = 0

def dfs(r, c, alpha, length):
    global gmax
    for dir in range(4):
        nr = r + x[dir]
        nc = c + y[dir]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in alpha:
            alpha.add(board[nr][nc])
            dfs(nr, nc, alpha, length + 1)
            alpha.remove(board[nr][nc])
    gmax = max(gmax, len(alpha))

dfs(0, 0, alpha, 1)

print(gmax)