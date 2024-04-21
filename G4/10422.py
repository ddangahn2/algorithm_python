# G4 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

import sys
input = sys.stdin.readline

T = int(input())

dp = [0 for _ in range(5001)]
dp[0] = dp[2] = 1
for i in range(4, 5001, 2):
    for j in range(2, i + 1, 2):
        dp[i] += dp[j - 2] * dp[i - j]
    dp[i] %= 1000000007
for _ in range(T):
    L = int(input())
    if L % 2 == 1:
        print(0)
    else:
        print(dp[L])