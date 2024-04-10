# G5 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

import sys
input = sys.stdin.readline

N = int(input())

board = [[1_500_000, 0]]
for i in range(N):
    # time, price
    T, P = map(int, input().split())
    board.append([T, P])
board.append([1_500_000, 0])

# 일한 다음날 돈 지급
dp = [0 for _ in range(N+2)]
for i in range(1, N+2):
    # 현재 자리 선택
    dp[i] = max(dp[i-1], dp[i])
    
    if i + board[i][0] <= N+1:
        dp[i + board[i][0]] = max(dp[i + board[i][0]], dp[i] + board[i][1])

print(dp[N+1])