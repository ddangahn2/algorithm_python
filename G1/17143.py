# G1 틀렸습니다
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

x_pos = [-1, 1, 0, 0]
y_pos = [0, 0, 1, -1]

board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    # (r,c) speed, dir, size
    r, c, s, d, z = map(int, input().split())
    if d in [0,1]:
        s %= 2 * (R-1)
    elif d in [2,3]:
        s %= 2 * (C-1)
    board[r-1][c-1] = [x_pos[d-1], y_pos[d-1], s, z]

catch_shark_size = 0

def fishman_catch_shark(idx):
    global catch_shark_size

    for i in range(R):
        if board[i][idx] != []:
            catch_shark_size += board[i][idx][3]
            board[i][idx] = []
            break
    
def shark_move():
    global board
    new_board = [[[] for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if board[i][j] != []:
                x, y = i, j
                x_dir, y_dir, s, z = board[i][j]
                for _ in range(s):
                    if (not 0 <= x + x_dir < R) or (not 0 <= y + y_dir < C):
                        x_dir = -x_dir
                        y_dir = -y_dir
                    x += x_dir
                    y += y_dir
                if new_board[x][y] == []:
                    new_board[x][y] = [x_dir, y_dir, s, z]
                else:
                    if new_board[x][y][3] < z:
                        new_board[x][y] = [x_dir, y_dir, s, z]
    board = new_board

def print_board(position):
    print(position)
    for i in range(R):
        for j in range(C):
            print(board[i][j], end=' ')
        print()
    print()

for pos in range(C):
    # i번째 자리 상어 잡기
    fishman_catch_shark(pos)
    # 이동
    shark_move()

print(catch_shark_size)