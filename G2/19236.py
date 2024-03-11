# G2 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
import copy
input = sys.stdin.readline

char = ["↑", "↖", "←", "↙", "↓", "↘", "→", "↗"]
x = [-1,-1,0,1,1,1,0,-1]
y = [0,-1,-1,-1,0,1,1,1]

board = []
total = 0
for _ in range(4):
    line = list(map(int, input().split()))
    board_row = []
    for i in range(4):
        board_row.append([line[i*2], line[i*2+1]-1])
    board.append(board_row)

def print_board(board):
    print()
    for i in board:
        for j in i:
            print(j[0], char[j[1]], end=' ')
        print()

def fish_move_board(shark_x, shark_y, score, board):
    global total
    score += board[shark_x][shark_y][0]
    board[shark_x][shark_y][0] = -1
    total = max(total, score)
    # shark를 -1로 표시
    fish = {}
    fish_index = []
    for i in range(4):
        for j in range(4):
            if board[i][j][0] > 0:
                fish[board[i][j][0]] = [i, j]
                fish_index.append(board[i][j][0])
    # fish dict sort
    sorted_fish = dict(sorted(fish.items()))
    fish_index.sort()
    
    for i in fish_index:
        fish_x, fish_y = sorted_fish[i]
        fish_pos = board[fish_x][fish_y][1]
        while (0 > fish_x + x[fish_pos] or fish_x + x[fish_pos] >= 4) or (0 > fish_y + y[fish_pos] or fish_y + y[fish_pos] >= 4) or board[fish_x + x[fish_pos]][fish_y + y[fish_pos]][0] == -1:
            fish_pos += 1
            fish_pos %= 8
        board[fish_x][fish_y][1] = fish_pos
        sw_fish = board[fish_x + x[fish_pos]][fish_y + y[fish_pos]][0]
        board[fish_x][fish_y], board[fish_x + x[fish_pos]][fish_y + y[fish_pos]] = board[fish_x + x[fish_pos]][fish_y + y[fish_pos]], board[fish_x][fish_y]
        
        sorted_fish[i][0] += x[fish_pos]
        sorted_fish[i][1] += y[fish_pos]
        if sw_fish != 0:
            sorted_fish[sw_fish][0] -= x[fish_pos]
            sorted_fish[sw_fish][1] -= y[fish_pos]
    shark_dir = board[shark_x][shark_y][1]
    board[shark_x][shark_y][0] = 0
    for i in range(1, 5):
        new_shark_x = shark_x + x[shark_dir]*i
        new_shark_y = shark_y + y[shark_dir]*i
        if 0 <= new_shark_x < 4 and 0 <= new_shark_y < 4 and board[new_shark_x][new_shark_y][0] > 0:
            fish_move_board(new_shark_x, new_shark_y, score, copy.deepcopy(board))
fish_move_board(0, 0, total, board)

print(total)