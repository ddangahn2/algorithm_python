# G5 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

N = int(input())
student = {}
seat = []
for _ in range(N**2):
    me, f1, f2, f3, f4 = map(int, input().split())
    student[me] = [f1,f2,f3,f4]
    seat.append(me)
board = [[0 for _ in range(N)] for _ in range(N)]
want_board = [[0 for _ in range(N)] for _ in range(N)]
#1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
#2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
#3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 쭉 돌면서 좋아하는 학생과 비어있는칸 체크
# 좋아하는 학생보다 크거나 같을떄 비어있는칸이 더 클 경우 체크

def seatdown(s):
    friend = -1
    blank  = -1
    pos_x = 0
    pos_y = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            temp_friend = 0
            temp_blank  = 0
            if i-1 >= 0:
                if board[i-1][j] == 0:
                    temp_blank += 1
                else:
                    if board[i-1][j] in student[s]:
                        temp_friend += 1
            if i+1 < N:
                if board[i+1][j] == 0:
                    temp_blank += 1
                else:
                    if board[i+1][j] in student[s]:
                        temp_friend += 1
            if j-1 >= 0:
                if board[i][j-1] == 0:
                    temp_blank += 1
                else:
                    if board[i][j-1] in student[s]:
                        temp_friend += 1
            if j+1 < N:
                if board[i][j+1] == 0:
                    temp_blank += 1
                else:
                    if board[i][j+1] in student[s]:
                        temp_friend += 1
            
            if temp_friend > friend:
                friend = temp_friend
                blank  = temp_blank
                pos_x = i
                pos_y = j
            elif temp_friend == friend and temp_blank > blank:
                blank = temp_blank
                pos_x = i
                pos_y = j
    board[pos_x][pos_y] = s
    return pos_x, pos_y

def want(r, c):
    if r-1 >= 0:
        if board[r-1][c] != 0:
            if board[r][c] in student[board[r-1][c]]:
                want_board[r-1][c] += 1
            if board[r-1][c] in student[board[r][c]]:
                want_board[r][c] += 1
    if r+1 < N:
        if board[r+1][c] != 0:
            if board[r][c] in student[board[r+1][c]]:
                want_board[r+1][c] += 1
            if board[r+1][c] in student[board[r][c]]:
                want_board[r][c] += 1
    if c-1 >= 0:
        if board[r][c-1] != 0:
            if board[r][c] in student[board[r][c-1]]:
                want_board[r][c-1] += 1
            if board[r][c-1] in student[board[r][c]]:
                want_board[r][c] += 1
    if c+1 < N:
        if board[r][c+1] != 0:
            if board[r][c] in student[board[r][c+1]]:
                want_board[r][c+1] += 1
            if board[r][c+1] in student[board[r][c]]:
                want_board[r][c] += 1

def result():
    res = 0
    for i in range(N):
        for j in range(N):
            if want_board[i][j] != 0:
                res += 10 ** (want_board[i][j] - 1)
    return res

def print_board():
    print()
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def print_want_board():
    print()
    for i in range(N):
        for j in range(N):
            print(want_board[i][j], end=' ')
        print()

for i in seat:
    r, c = seatdown(i)
    want(r, c)
print(result())