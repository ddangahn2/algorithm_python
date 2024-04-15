# S1 solved
# [대기업 코테에서 나오는 유형 모음](https://www.acmicpc.net/workbook/view/8708)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

n = [0 for _ in range(200_001)]
a_list = list(map(int, input().split()))

st = 0
ed = 0
max_length = 0
temp_length = 0
while st < N:
    if n[a_list[st]] < K:
        n[a_list[st]] += 1
        st += 1
        temp_length += 1
    else:
        max_length = max(max_length, temp_length)
        while n[a_list[st]] >= K:
            n[a_list[ed]] -= 1
            ed += 1
            temp_length -= 1
max_length = max(max_length, temp_length)
print(max_length)