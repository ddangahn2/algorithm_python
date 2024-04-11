# G4 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

import sys
input = sys.stdin.readline

dp = [-1 for _ in range(10_001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

# dp[i-3]은 i를 표현할 때 3이 들어가면서 포현되는 방법이다
# 그 이후에는 3이 포함되면 위에 표현과 겹치게 되므로 2와 1로만 i를 표현해야하고
# 그 방법은 (i//2 + 1)개이다.
for i in range(4, 10_001):
    dp[i] = dp[i-3] + (i//2 + 1)

N = int(input())
for _ in range(N):
    print(dp[int(input())])