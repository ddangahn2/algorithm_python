# G4 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 0위, 1오, 2아, 3왼
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]
ch_dir = [2, 3, 0, 1]


def open_door(r, c):
    # 해당 좌표에 0,1,2,3 기록
    for dir in range(4):
        nr = r + x[dir]
        nc = c + y[dir]
        if 0 <= nr < N and 0 <= nc < N and L <= abs(board[r][c] - board[nr][nc]) <= R:
            if (r, c) not in open_dict:
                open_dict[(r, c)] = set()
            open_dict[(r, c)].add(dir)
            if (nr, nc) not in open_dict:
                open_dict[(nr, nc)] = set()
            open_dict[(nr, nc)].add(ch_dir[dir])
    
def change_population(r, c):
    global visited
    # 인접한 칸들 모두 체크
    position   = []
    population = 0

    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()

        position.append((cr, cc))
        population += board[cr][cc]

        if (cr, cc) in open_dict:
            for dir in open_dict[(cr, cc)]:
                nr = cr + x[dir]
                nc = cc + y[dir]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    population //= len(position)
    for con_x, con_y in position:
        board[con_x][con_y] = population

def print_board():
    print()
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

day = 0
while True:
    open_dict = {}
    for i in range(N):
        for j in range(N):
            open_door(i, j)
    if len(open_dict) != 0:
        day += 1
    else:
        print(day)
        exit(0)
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                change_population(i, j)