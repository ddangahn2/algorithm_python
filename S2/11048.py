# S2 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
for i in reversed(range(N)):
    for j in reversed(range(M)):
        if i == N-1 and j == M-1:
            dp[i][j] = board[i][j]
        elif i == N-1:
            dp[i][j] = board[i][j] + dp[i][j+1]
        elif j == M-1:
            dp[i][j] = board[i][j] + dp[i+1][j]
        else:
            dp[i][j] = board[i][j] + max(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])