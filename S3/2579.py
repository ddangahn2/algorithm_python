# S3 solved

import sys
input = sys.stdin.readline

N = int(input())
step = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
# 1 or 2
# 시작점 계단 x
# last O

dp[0] = step[0]
if N == 1:
    print(dp[N-1])
    exit(0)

dp[1] = step[0] + step[1]
if N == 2:
    print(dp[N-1])
    exit(0)

dp[2] = max(dp[0] + step[2], step[1] + step[2])
if N == 3:
    print(dp[N-1])
    exit(0)

for i in range(3, N):
    dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])

print(dp[N-1])