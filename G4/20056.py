# G4 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

fire_ball = []

x = [-1,-1,0,1,1,1,0,-1]
y = [0,1,1,1,0,-1,-1,-1]

for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    fire_ball.append([r-1, c-1, m, s, d])


board = [[[] for _ in range(N)] for _ in range(N)]

def init():
    for r,c,m,s,d in fire_ball:
        board[r][c].append([m,s,d])

def fire_ball_move():
    global board
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            while board[i][j]:
                m, s, d = board[i][j].pop()
                ni = i + x[d] * s
                nj = j + y[d] * s
                ni %= N
                nj %= N
                new_board[ni][nj].append([m, s, d])
    board = new_board

def fire_ball_pop():
    global board
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                mass = 0
                speed = 0
                pos = (board[i][j][0][2] % 2)
                pos_change = 0
                for k in range(len(board[i][j])):
                    m, s, d = board[i][j][k]
                    mass += m
                    speed += s
                    if pos != (d % 2):
                        pos_change = 1
                mass //= 5
                speed //= len(board[i][j])

                if mass == 0:
                    continue
                else:
                    for p in range(0, 7, 2):
                        new_board[i][j].append([mass, speed, p + pos_change])
            elif len(board[i][j]) == 1:
                new_board[i][j].append([board[i][j][0][0], board[i][j][0][1], board[i][j][0][2]])
    board = new_board

def print_board():
    global board
    print()
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def add_fireball():
    res = 0
    for i in range(N):
        for j in range(N):
            while board[i][j]:
                m, s, d = board[i][j].pop()
                res += m
    return res

init()
for _ in range(K):
    fire_ball_move()
    fire_ball_pop()

print(add_fireball())