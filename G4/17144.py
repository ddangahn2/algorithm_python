# G4 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

clean_top_x = 0
clean_top_y = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            board[i][j] = 0
            clean_top_x = i
            clean_top_y = j
            break
clean_top_x -= 1
clean_down_x = clean_top_x + 1
clean_down_y = clean_top_y
clean_pos = [(clean_top_x, clean_top_y), (clean_down_x, clean_down_y)]

x = [-1,1,0,0]
y = [0,0,-1,1]

def spread():
    global board
    spread_board = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] >= 5:
                spread_count = 0
                for dir in range(4):
                    ni = i + x[dir]
                    nj = j + y[dir]
                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in clean_pos:
                        spread_count += 1
                        spread_board[ni][nj] += (board[i][j] // 5)
                spread_board[i][j] += (board[i][j]) - ((board[i][j] // 5) * spread_count)
            else:
                spread_board[i][j] += board[i][j]
    board = spread_board

def air_clean():
    # air_top
    air_top_x = clean_top_x
    air_top_y = clean_top_y
    # 위로
    while air_top_x > 0:
        board[air_top_x][air_top_y] = board[air_top_x - 1][air_top_y]
        air_top_x -= 1
    # 오른쪽으로
    while air_top_y < C-1:
        board[air_top_x][air_top_y] = board[air_top_x][air_top_y + 1]
        air_top_y += 1
    # 아래로
    while air_top_x < clean_top_x:
        board[air_top_x][air_top_y] = board[air_top_x + 1][air_top_y]
        air_top_x += 1
    # 왼쪽으로
    while air_top_y > 0:
        board[air_top_x][air_top_y] = board[air_top_x][air_top_y - 1]
        air_top_y -= 1
        
    # air_down
    air_down_x = clean_down_x
    air_down_y = clean_down_y
    # 아래로
    while air_down_x < R - 1:
        board[air_down_x][air_down_y] = board[air_down_x + 1][air_down_y]
        air_down_x += 1
    # 오른쪽으로
    while air_down_y < C - 1:
        board[air_down_x][air_down_y] = board[air_down_x][air_down_y + 1]
        air_down_y += 1
    # 위로
    while air_down_x > clean_down_x:
        board[air_down_x][air_down_y] = board[air_down_x - 1][air_down_y]
        air_down_x -= 1
    # 왼쪽으로
    while air_down_y > 0:
        board[air_down_x][air_down_y] = board[air_down_x][air_down_y - 1]
        air_down_y -= 1
    
    for clean in clean_pos:
        board[clean[0]][clean[1]] = 0
        board[clean[0]][clean[1] + 1] = 0

def print_board():
    print()
    for i in range(R):
        for j in range(C):
            print(board[i][j], end=' ')
        print()

def answer():
    ans = 0
    for i in range(R):
        for j in range(C):
            ans += board[i][j]
    return ans

for i in range(T):
    spread()
    air_clean()
    # print_board()
print(answer())