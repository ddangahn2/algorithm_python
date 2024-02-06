# S1 solved

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

area_nums = set()
for i in range(N):
    area_nums |= set(area[i])

area_nums = list(area_nums)

global_area_count = 1

x = [-1,1,0,0]
y = [0,0,-1,1]
# 해당 위치부터 bfs
def bfs(r, c, num):
    q = deque()
    q.append((r, c))
    while q:
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + x[dir]
            nc = cc + y[dir]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and area[nr][nc] > num:
                visited[nr][nc] = True
                q.append((nr, nc))

for num in area_nums:
    local_area_count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > num:
                visited[i][j] = True
                local_area_count += 1
                bfs(i, j, num)
    global_area_count = max(global_area_count, local_area_count)

print(global_area_count)