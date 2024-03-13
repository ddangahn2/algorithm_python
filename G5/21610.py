# G5 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
input = sys.stdin.readline

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
x = [0,-1,-1,-1,0,1,1,1]
y = [-1,-1,0,1,1,1,0,-1]


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
turn = []
for _ in range(M):
    d, s = map(int, input().split())
    turn.append([d-1, s])

cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
cloud_visit = [[False for _ in range(N)] for _ in range(N)]

def move_cloud(d, s):
    for i in range(len(cloud)):
        cloud[i][0] += (x[d] * s)
        cloud[i][1] += (y[d] * s)
        cloud[i][0] %= N
        cloud[i][1] %= N
        
        cloud_visit[cloud[i][0]][cloud[i][1]] = True

def cloud_rain():
    for i in cloud:
        board[i[0]][i[1]] += 1

def water_magic():
    for i in cloud:
        temp = 0
        x = i[0]
        y = i[1]
        if 0 <= x-1 and 0 <= y-1 and board[x-1][y-1]:
            temp += 1
        if 0 <= x-1 and N > y+1 and board[x-1][y+1]:
            temp += 1
        if N > x+1 and 0 <= y-1 and board[x+1][y-1]:
            temp += 1
        if N > x+1 and N > y+1 and board[x+1][y+1]:
            temp += 1
        board[x][y] += temp

def make_cloud():
    global cloud
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and cloud_visit[i][j] == False:
                board[i][j] -= 2
                new_cloud.append([i, j])
            else:
                cloud_visit[i][j] = False
    cloud = new_cloud

def print_board():
    print()
    for i in board:
        for j in i:
            print(j, end=' ')
        print()

def add_water():
    ans = 0
    for i in board:
        for j in i:
            ans += j
    return ans

for d, s in turn:
    # print_board()
    move_cloud(d, s)
    cloud_rain()
    water_magic()
    make_cloud()

print(add_water())