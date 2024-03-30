# P5 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

# 윗면 흰색, 아래 노란, 앞 빨간, 뒤 오렌지, 왼 초, 오른 파

import sys
input = sys.stdin.readline

T = int(input())
             
#            up(0,w)
#             0 1 2
#             3 4 5
#             6 7 8
# 
#  left(4,g)  fr(2,r)  right(5,b)
#   0 1 2     0 1 2     0 1 2
#   3 4 5     3 4 5     3 4 5
#   6 7 8     6 7 8     6 7 8
#              
#            back(3,o)
#             6 7 8 
#             3 4 5
#             0 1 2
#              
#            down(1,y)
#             6 7 8
#             3 4 5
#             0 1 2

cube_face = {"U":[0,[(4, 2), (4, 1), (4, 0), (3, 6), (3, 7), (3, 8), (5, 2), (5, 1), (5, 0), (2, 2), (2, 1), (2, 0)]],
             "D":[1,[(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (5, 6), (5, 7), (5, 8), (3, 2), (3, 1), (3, 0)]],
             "F":[2,[(0, 6), (0, 7), (0, 8), (5, 0), (5, 3), (5, 6), (1, 2), (1, 1), (1, 0), (4, 8), (4, 5), (4, 2)]],
             "B":[3,[(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (1, 6), (1, 7), (1, 8), (5, 8), (5, 5), (5, 2)]],
             "L":[4,[(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (1, 0), (1, 3), (1, 6), (3, 0), (3, 3), (3, 6)]],
             "R":[5,[(0, 8), (0, 5), (0, 2), (3, 8), (3, 5), (3, 2), (1, 8), (1, 5), (1, 2), (2, 8), (2, 5), (2, 2)]]}

def move(face, clockwise):
    rot1, rot2 = cube_face[face]
    if clockwise == False:
        rot2 = list(reversed(rot2))
    rot_face(rot1, clockwise)
    rot_body(rot2)

#                  default
#                     ↓
# 2 5 8  !clockwise 0 1 2 clockwise 6 3 0
# 1 4 7      <-     3 4 5    ->     7 4 1
# 0 3 6             6 7 8           8 5 2
def rot_face(face_num, clockwise):
    global cube
    temp_cube = []
    for i in range(9):
        temp_cube.append(cube[face_num][i])
    if clockwise:
        cube[face_num][0], cube[face_num][1], cube[face_num][2], cube[face_num][3], cube[face_num][4], cube[face_num][5], cube[face_num][6], cube[face_num][7], cube[face_num][8] = temp_cube[6], temp_cube[3], temp_cube[0], temp_cube[7], temp_cube[4], temp_cube[1], temp_cube[8], temp_cube[5], temp_cube[2]
    else:
        cube[face_num][0], cube[face_num][1], cube[face_num][2], cube[face_num][3], cube[face_num][4], cube[face_num][5], cube[face_num][6], cube[face_num][7], cube[face_num][8] = temp_cube[2], temp_cube[5], temp_cube[8], temp_cube[1], temp_cube[4], temp_cube[7], temp_cube[0], temp_cube[3], temp_cube[6]

def rot_body(rot_face_list):
    global cube
    # 총 12개 0 3 6 9, 1 4 7 10, 2 5 8 11 이렇게 3개 한칸씩 미뤄야함.
    spin = [3,0,1,2]
    for i in range(3):
        temp = []
        for j in range(4):
            idx = i + 3*j
            temp.append(cube[rot_face_list[idx][0]][rot_face_list[idx][1]])
        for j in range(4):
            idx = i + 3*j
            cube[rot_face_list[idx][0]][rot_face_list[idx][1]] = temp[spin[j]]

def print_board():
    for f in range(1):
        for i in range(1,10):
            print(cube[f][i-1], end='')
            if i % 3 == 0:
                print()
    

for _ in range(T):
    n = int(input())
    m = list(input().strip().split())
    cube = [["w"] * 9, ["y"] * 9, ["r"] * 9, ["o"] * 9, ["g"] * 9, ["b"] * 9]
    for t in m:
        if t[1] == "+":
            move(t[0], True)
        else:
            move(t[0], False)
    print_board()