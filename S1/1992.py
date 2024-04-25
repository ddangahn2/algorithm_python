# S1 solved

import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

res = ""

def check(st_x, st_y, ed_x, ed_y):
    point = board[st_x][st_y]
    for i in range(st_x, ed_x):
        for j in range(st_y, ed_y):
            if board[i][j] != point:
                return False
    return True

def qt_zip(st_x, st_y, ed_x, ed_y, size):
    global res
    
    if check(st_x, st_y, ed_x, ed_y):
        res += board[st_x][st_y]
    else:
        res += "("
        qt_zip(st_x, st_y, ed_x - size//2, ed_y - size//2, size//2)
        qt_zip(st_x, st_y + size//2, ed_x - size//2, ed_y, size//2)
        qt_zip(st_x + size//2, st_y, ed_x, ed_y - size//2, size//2)
        qt_zip(st_x + size//2, st_y + size//2, ed_x, ed_y, size//2)
        res += ")"
    

qt_zip(0,0,N,N,N)
print(res)