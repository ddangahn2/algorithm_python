# G3 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

virus = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i,j])

x_pos = [-1,1,0,0]
y_pos = [0,0,-1,1]

def bfs(combi):
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    q = deque()
    for i in combi:
        q.append(virus[i])
        visited[virus[i][0]][virus[i][1]] = 0
    count = 0
    while q:
        cx, cy = q.popleft()
        for pos in range(4):
            nx = cx + x_pos[pos]
            ny = cy + y_pos[pos]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1
                count = max(count, visited[nx][ny])
                q.append([nx, ny])
    res = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] == 0:
                return -1
            elif board[i][j] == 0:
                res = max(res, visited[i][j])
    return res

ans = set()
for i in combinations([_ for _ in range(len(virus))], M):
    ans.add(bfs(i))
ans.add(-1)
ans = list(ans)
if ans == [-1]:
    print(-1)
else:
    ans.remove(-1)
    print(min(ans))