# G3 solved

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

if n == 1:
    print(0)
else:
    for i in range(n-1):
        dp[i][i+1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]
    for i in range(2, n):
        for j in range(0, n-i):
            dp[j][j+i] = min([dp[j][j+k] + dp[j+k+1][j+i] + matrix[j][0] * matrix[j+k][1] * matrix[j+i][1] for k in range(i)])
    
    print(dp[0][n-1])