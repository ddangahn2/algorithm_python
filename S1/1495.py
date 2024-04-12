# S1 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

import sys
input = sys.stdin.readline

# 곡개수, 시작볼륨, 최대볼륨
N, S, M = map(int, input().split())
vol = list(map(int, input().split()))

possible_vol = [S]
for i in range(N):
    possible_vol_set = set()

    while possible_vol:
        temp_vol = possible_vol.pop()
        if temp_vol + vol[i] <= M:
            possible_vol_set.add(temp_vol + vol[i])
        if temp_vol - vol[i] >= 0:
            possible_vol_set.add(temp_vol - vol[i])
    
    possible_vol = list(possible_vol_set)

if len(possible_vol) == 0:
    print(-1)
else:
    possible_vol.sort()
    print(possible_vol[-1])