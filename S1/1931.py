# S1 solved

import sys
input = sys.stdin.readline

N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
T.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end = T[0][1]

for i in range(1, N):
    if T[i][0] >= end:
        cnt += 1
        end = T[i][1]
print(cnt)