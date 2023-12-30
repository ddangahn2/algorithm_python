# G5 solved

N, K = map(int, input().split())

# 가로 K+1 세로 N+1 배열 만들기
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# 가방과 가치 입력 받아서 정렬
bags = []
for i in range(N):
    W, V = map(int, input().split())
    bags.append([W, V])
bags.sort(key=lambda bag: bag[0])

# 가방 하나씩 추가시키면서 DP
for index, bag in enumerate(bags):
    W, V = bag
    for lift_weight in range(K+1):
        if lift_weight < W:
            dp[index + 1][lift_weight] = dp[index][lift_weight]
        else:
            dp[index + 1][lift_weight] = max(dp[index][lift_weight], V + dp[index][lift_weight - W])

print(dp[N][K])