# G4 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())

board = [[0 for _ in range(100)] for _ in range(100)]
r = 3
c = 3
for i in range(r):
    A = list(map(int, input().split()))
    for j in range(c):
        board[i][j] = A[j]

def row():
    global c, board
    # 정렬
    max_col = 0
    new_board = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(r):
        temp_dict = {}
        for j in range(c):
            if board[i][j] == 0:
                continue
            if board[i][j] not in temp_dict:
                temp_dict[board[i][j]] = 1
            else:
                temp_dict[board[i][j]] += 1
        171
        tcol = 0
        temp_list = sorted(list(temp_dict.items()), key=lambda x: (x[1], x[0]))
        # temp_list.sort(key=lambda x:x[1])
        for num, count in temp_list:
            new_board[i][tcol] = num
            tcol += 1
            new_board[i][tcol] = count
            tcol += 1
            if tcol == 100:
                break
        max_col = max(max_col, tcol)
    c = max_col
    board = new_board
         
def col():
    global r, board
    # 정렬
    max_row = 0
    new_board = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(c):
        temp_dict = {}
        for j in range(r):
            if board[j][i] == 0:
                continue
            if board[j][i] not in temp_dict:
                temp_dict[board[j][i]] = 1
            else:
                temp_dict[board[j][i]] += 1
        
        trow = 0
        temp_list = sorted(list(temp_dict.items()), key=lambda x: (x[1], x[0]))
        # temp_list.sort(key=lambda x:x[1])
        for num, count in temp_list:
            new_board[trow][i] = num
            trow += 1
            new_board[trow][i] = count
            trow += 1
            if trow == 100:
                break
        max_row = max(max_row, trow)
    r = max_row
    board = new_board

def print_board():

    for i in range(10):
        for j in range(10):
            print(board[i][j], end=' ')
        print()
    print()

time = 0
while time <= 100:
    if board[R-1][C-1] == K:
        print(time)
        exit(0)
    if r >= c:
        row()
    else:
        col()
    time += 1
print(-1)