# G1 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

input_board = [list(map(int, input().split())) for _ in range(N)]
board = []
ds = []
for _ in range(M):
    D, S = map(int, input().split())
    ds.append((D, S))

# 일단 일렬료
# 위, 아래, 왼, 오
# 처음부터 빼니까 앞에부터 0, 1, 2, 3 뺴면 된다. (빼면 index가 당겨지기 때문)
ds_pop = [[7, 22, 45, 76, 115, 162, 217, 280, 351, 430, 517, 612, 715, 826, 945, 1072, 1207, 1350, 1501, 1660, 1827, 2002, 2185, 2376],
          [3, 14, 33, 60, 95, 138, 189, 248, 315, 390, 473, 564, 663, 770, 885, 1008, 1139, 1278, 1425, 1580, 1743, 1914, 2093, 2280]
          ,[1, 10, 27, 52, 85, 126, 175, 232, 297, 370, 451, 540, 637, 742, 855, 976, 1105, 1242, 1387, 1540, 1701, 1870, 2047, 2232]
          ,[5, 18, 39, 68, 105, 150, 203, 264, 333, 410, 495, 588, 689, 798, 915, 1040, 1173, 1314, 1463, 1620, 1785, 1958, 2139, 2328]]

for i in range(4):
    for j in range(len(ds_pop[0])):
        ds_pop[i][j] -= j

# 아래, 오른, 위, 왼
x = [1,0,-1,0]
y = [0,1,0,-1]

res = 0

def make_board():
    # input_board -> board
    st_x = st_y = (N-1)//2
    st_y -= 1
    dir = 0
    for i in range((N-1)//2):
        go = i*2+2
        for j in range(4):
            for k in range(go):
                # 직진
                if input_board[st_x][st_y] == 0:
                    return
                board.append(input_board[st_x][st_y])
                st_x += x[dir]
                st_y += y[dir]

                if k == go-1 and j != 3:
                    # 방향전환
                    st_x -= x[dir]
                    st_y -= y[dir]
                    dir += 1
                    dir %= 4
                    st_x += x[dir]
                    st_y += y[dir]
        # 방향전환
        dir += 1
        dir %= 4

def blizard(d, s):
    pop = ds_pop[d-1]
    # s개 pop
    for i in range(s):
        if pop[i] <= len(board):
            board.pop(pop[i]-1)
        
def pop_four():
    global res

    biz = 0
    count = 0
    pop = []
    for i in range(len(board)):
        if board[i] != biz:
            biz = board[i]
            count = 1
        else:
            count += 1
            if count == 4:
                pop.append(i-3)
                pop.append(i-2)
                pop.append(i-1)
                pop.append(i)
            elif count > 4:
                pop.append(i)
    pop.reverse()

    for i in pop:
        res += board.pop(i)

    if len(pop):
        return True
    return False

def biz_magic():
    global board
    new_board = []
    new_board_len = N ** 2 - 1
    if board == []:
        return
    
    biz = board[0]
    count = 0

    for i in range(len(board)):
        if board[i] == biz:
            count += 1
        elif new_board_len > 0:
            new_board.append(count)
            new_board.append(biz)
            biz = board[i]
            count = 1
            new_board_len -= 2

    if new_board_len > 0:
        new_board.append(count)
        new_board.append(biz)
    
    board = new_board

make_board()

for i in range(len(ds)):
    blizard(ds[i][0], ds[i][1])

    while pop_four():
        continue
    biz_magic()
print(res)