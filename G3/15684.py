# G3 solved

# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

from math import inf
# 세로선, 가로선, 높이
N, M, H = map(int, input().split())

# 사다리타기에 놓은 다리만 체크
board = [[False for _ in range(N)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True

min_count = inf

def action():
    for ans in range(N):
        play = ans
        for j in range(H):
            if board[j][play]:
                play += 1
            elif play > 0 and board[j][play - 1]:
                play -= 1
        if ans != play:
            return False
    return True

def print_board():
    print()
    for i in board:
        for j in i:
            print("|", end='')
            if j == False:
                print(" |", end='')
            else:
                print("-|", end='')
        print()

def dfs(count, latest_x, latest_y):
    global min_count
    if count >= 4:
        return
    else:
        if action():
            # print_board()
            min_count = min(min_count, count)
            return
        else:
            for i in range(latest_x, H):
                if i == latest_x:
                    now = latest_y
                else:
                    now = 0
                
                for j in range(now, N-1):
                    if not board[i][j] and not board[i][j+1]:
                        if j > 0 and board[i][j-1]:
                            continue
                        board[i][j] = True
                        dfs(count + 1, i, j + 2)
                        board[i][j] = False

if action():
    print(0)
    exit(0)
dfs(0, -1, -1)

if min_count == inf:
    print(-1)
else:
    print(min_count)
