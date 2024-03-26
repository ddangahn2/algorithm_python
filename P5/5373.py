# P5 solving
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

# 윗면 흰색, 아래 노란, 앞 빨간, 뒤 오렌지, 왼 초, 오른 파

import sys
input = sys.stdin.readline

T = int(input())

cube_face = {"U":[0,[(4, 2), (4, 1), (4, 0), (3, 2), (3, 1), (3, 0), (5, 2), (5, 1), (5, 0), (2, 2), (2, 1), (2, 0)]],"D":[1,[(4, 6), (4, 7), (4, 8),(2, 6), (2, 7), (2, 8), (5, 6), (5, 7), (5, 8), (3, 6), (3, 7), (3, 8)]],"F":[2,[(0, 6), (0, 7), (0, 8), (5, 0), (5, 3), (5, 6), (1, 6), (1, 7), (1, 8), (4, 8), (4, 5), (4, 2)]],"B":[3,[(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (1, 2), (1, 1), (1, 0), (5, 8), (5, 5), (5, 2)]],"L":[4,[(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (1, 8), (1, 5), (1, 2), (3, 8), (3, 5), (3, 2)]],"R":[5,[(0, 8), (0, 5), (0, 2), (3, 0), (3, 3), (3, 6), (1, 0), (1, 3), (1, 6), (2, 8), (2, 5), (2, 2)]]}
def move(face, clockwise):
    rot1, rot2 = cube_face[face]
    if clockwise == False:
        rot2.reverse()
    rot_face(rot1, clockwise)
    rot_body(rot2)

def rot_face(face_num, clockwise):
    global cube
    f = cube[face_num]
    if clockwise:
        f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[6], f[3], f[0], f[7], f[1], f[8], f[5], f[2]
    else:
        f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[2], f[5], f[8], f[1], f[7], f[0], f[3], f[6]

def rot_body(rot_face_list):
    global cube
    for i in range(3):
        c1 = rot_face_list[i]
        c2 = rot_face_list[i+3]
        c3 = rot_face_list[i+6]
        c4 = rot_face_list[i+9]
        cube[c1[0]][c1[1]], cube[c2[0]][c2[1]], cube[c3[0]][c3[1]], cube[c4[0]][c4[1]] = cube[c4[0]][c4[1]], cube[c1[0]][c1[1]], cube[c2[0]][c2[1]], cube[c3[0]][c3[1]]

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
    