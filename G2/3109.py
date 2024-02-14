# G2 solved

import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().strip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

x = [-1, 0, 1]
y = [1, 1, 1]
count = 0
def dfs(r, c):
    global count
    if c == C-1:
        count += 1
        return True
    else:
        for dir in range(3):
            nr = r + x[dir]
            nc = c + y[dir]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == ".":
                visited[nr][nc] = True
                if dfs(nr, nc):
                    return True
        return False

for i in range(R):
    visited[i][0] = True
    dfs(i, 0)

print(count)