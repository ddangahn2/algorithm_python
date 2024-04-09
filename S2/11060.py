# S2 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

import sys
input = sys.stdin.readline

N = int(input())
maze = list(map(int, input().split()))

start = 0
time = 0

if start == N-1:
    print(time)
    exit(0)

while start < N:
    time += 1
    jump_max = maze[start]

    temp_start = -1
    temp_max = 0
    # 다음 점프할 지점 찾기
    for i in range(start + 1, start + jump_max + 1):
        if i == N-1:
            print(time)
            exit(0)
        if i + maze[i] > temp_max:
            temp_max = i + maze[i]
            temp_start = i
    if temp_start == -1:
        print(-1)
        exit(0)
    start = temp_start