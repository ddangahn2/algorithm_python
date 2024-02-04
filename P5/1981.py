# P5 solved

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

std = arr[0][0]
x = [-1,1,0,0]
y = [0,0,-1,1]

def bfs(l, r):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    q = deque()
    q.append((0,0))

    while q:
        cx, cy = q.popleft()

        if cx == n-1 and cy == n-1:
            return True

        for dir in range(4):
            nx = cx + x[dir]
            ny = cy + y[dir]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= arr[nx][ny] <= r:
                q.append((nx, ny))
                visited[nx][ny] = True
    return False

diff = 1

minimum = 200

List = [-1 for _ in range(201)]

if bfs(std, std):
    List[1] = 0
    print(0)
else:
    while List[diff] == -1:
        # 안되면 2배
        # 되면 -1
        flag = 0
        for i in range(diff + 1):
            if std - diff + i < 0 or std + i > 200:
                continue
            if bfs(std - diff + i, std + i):
                minimum = min(minimum, diff)
                flag = 1
                break
        List[diff] = 1
        if flag:
            diff -= 1
        else:
            diff *= 2
            diff = min(200, diff)
    print(minimum)