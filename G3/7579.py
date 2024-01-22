# G3 solved

N, M = map(int, input().split())

A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

minimum = 10000
total_cost = 0
for i in C:
    total_cost += i

dp = [[0 for _ in range(total_cost+1)] for _ in range(N+1)]

for i in range(1,N+1):
    mem  = A[i]
    cost = C[i]

    for j in range(total_cost+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], mem + dp[i-1][j-cost])
            if dp[i][j] >= M:
                minimum = min(minimum, j)

print(minimum)