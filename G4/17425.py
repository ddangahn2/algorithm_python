# G4 solved
# [코딩 테스트 준비 - 기초](https://www.acmicpc.net/workbook/view/9370)

import sys
input = sys.stdin.readline

T = int(input())

gx = [1] * 1_000_001
fx = [1] * 1_000_001

for i in range(2, 1_000_001):
    j = 1
    while i * j <= 1_000_000:
        fx[i * j] += i
        j += 1
    gx[i] = gx[i - 1] + fx[i]

for i in range(T):
    print(gx[int(input())])