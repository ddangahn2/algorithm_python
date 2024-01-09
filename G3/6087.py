# G3 solved

w, h = map(int, input().split())

tmap = [list(input()) for _ in range(h)]

c1_x = -1
c1_y = -1

c2_x = -1
c2_y = -1

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

cur_move = []
next_move = []

# 2개의 c 위치 찾기
def whereIsC():
    global c1_x, c1_y, c2_x, c2_y
    for row in range(h):
        for col in range(w):
            if tmap[row][col] == 'C':
                if c1_x == -1:
                    c1_x = row
                    c1_y = col
                    cur_move.append((row, col))
                    tmap[row][col] = 0
                else:
                    c2_x = row
                    c2_y = col
                    tmap[row][col] = '.'
                    break

# 현재 위치에서 상하좌우로 이동
def lazer_move(row, col):
    depth = tmap[row][col]

    for dir in range(4):
        n_row = row + x[dir]
        n_col = col + y[dir]

        while 0 <= n_row < h and 0 <= n_col < w and tmap[n_row][n_col] != '*':
            if tmap[n_row][n_col] == '.':
                tmap[n_row][n_col] = depth + 1
                next_move.append((n_row, n_col))
            n_row += x[dir]
            n_col += y[dir]                

# 레이저가 다른 c에 도달했는지 확인
def is_reached():
    if tmap[c2_x][c2_y] != '.':
        print(tmap[c2_x][c2_y] - 1)
        return False
    return True


whereIsC()

while is_reached():
    for row, col in cur_move:
        lazer_move(row, col)
    cur_move = next_move
    next_move = []