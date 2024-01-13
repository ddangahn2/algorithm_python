# G3 solved

test_case = int(input())

for test in range(test_case):
    K = int(input())

    data = list(map(int, input().split()))

    part_sum = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(K):
        for j in range(i, K):
            if i == j:
                part_sum[i][j] = data[i]
            else:
                part_sum[i][j] = part_sum[i][j-1] + data[j]

    dp = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(K):
        dp[i][i] = data[i]
    for i in range(K-1):
        dp[i][i+1] = part_sum[i][i+1]

    for i in range(2, K):
        for j in range(K - i):
            least = min(dp[j+1][j+i] + part_sum[j][j+i], dp[j][j+i-1] + part_sum[j][j+i])
            for k in range(j+1, j+i-1):
                least = min(least, dp[j][k] + dp[k+1][j+i] + part_sum[j][j+i])
            dp[j][j+i] = least

    print(dp[0][K-1])