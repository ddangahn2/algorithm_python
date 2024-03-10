# G3 solved

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

sh_x = 0
sh_y = 0
sh_size = 2
eat_count = 0
time = 0
# 위, 왼, 오, 아래
x = [-1,0,0,1]
y = [0,-1,1,0]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sh_x = i; sh_y = j

def bfs(sh_x, sh_y):
    global sh_size, eat_count
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sh_x][sh_y] = True
    q = deque()
    q.append((sh_x, sh_y, 0))
    board[sh_x][sh_y] = 0

    catch_pos = []
    while q:
        cur_sh_x, cur_sh_y, cur_time = q.popleft()
        for dir in range(4):
            new_sh_x = cur_sh_x + x[dir]
            new_sh_y = cur_sh_y + y[dir]
            if 0 <= new_sh_x < N and 0 <= new_sh_y < N and not visited[new_sh_x][new_sh_y] and board[new_sh_x][new_sh_y] <= sh_size:
                if 0 < board[new_sh_x][new_sh_y] < sh_size:
                    catch_pos.append((new_sh_x, new_sh_y, cur_time + 1))
                elif catch_pos == []:
                    q.append((new_sh_x, new_sh_y, cur_time + 1))
                    visited[new_sh_x][new_sh_y] = True
    if catch_pos != []:
        eat_count += 1
        if eat_count == sh_size:
            eat_count = 0
            sh_size += 1
        catch_pos.sort(key = lambda x: (x[2],x[0],x[1]))
        board[catch_pos[0][0]][catch_pos[0][1]] = 9
        return catch_pos[0][0], catch_pos[0][1], catch_pos[0][2]
    return -1, -1, -1

while True:
    sh_x, sh_y, cur_time = bfs(sh_x, sh_y)
    if sh_x == -1 and sh_y == -1:
        break
    time += cur_time
print(time)