# G5 solved


# 각 치킨집에서 집까지 거리 계산 bfs
# 모든 치킨집을 콤비네이션하고, 
#   각 치킨집에 거리 최소값으로 치킨거리 계산

import sys
from collections import deque
from itertools import combinations
from math import inf
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 구하기
chicken = []
house = []
min_distance = inf
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i, j))
        elif board[i][j] == 1:
            house.append((i, j))

chicken_house = [[[[-1 for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
x = [-1,1,0,0]
y = [0,0,-1,1]

def bfs(ch_x, ch_y):
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((ch_x, ch_y))
    dist[ch_x][ch_y] = 0

    while q:
        ch_cx, ch_cy = q.popleft()
        for dir in range(4):
            ch_nx = ch_cx + x[dir]
            ch_ny = ch_cy + y[dir]
            if 0 <= ch_nx < N and 0 <= ch_ny < N and dist[ch_nx][ch_ny] == -1:
                q.append((ch_nx, ch_ny))
                dist[ch_nx][ch_ny] = dist[ch_cx][ch_cy] + 1
                if board[ch_nx][ch_ny] == 1:
                    chicken_house[ch_x][ch_y][ch_nx][ch_ny] = dist[ch_cx][ch_cy] + 1

def chicken_distance(ch_combi):
    distance_list = []
    for ho in house:
        temp_min = inf
        for ch in ch_combi:
            temp_min = min(temp_min, chicken_house[ch[0]][ch[1]][ho[0]][ho[1]])
        distance_list.append(temp_min)
    return sum(distance_list)

for ch in chicken:
    bfs(ch[0], ch[1])

chicken_combination = combinations(chicken, M)

for ch_combi in chicken_combination:
    min_distance = min(min_distance, chicken_distance(ch_combi))

print(min_distance)