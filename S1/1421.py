# S1 solved

import sys
input = sys.stdin.readline

# 나무개수 N개, 자를떄비용 C, 나무 한단위 가격 W
N, C, W = map(int, input().split())

# 나무 개수 N <= 50이고, 나무 길이 10,000보다 작다
# 길이에 대해 1 ~ 10000까지 모두 해본다면?
log = []
for i in range(N):
    tree = int(input())
    log.append(tree)

max_price = 0
for i in range(1, 10001):
    temp_cost = 0
    # 단위나무 * 나뉜개수 * W - 몇번 자르는지 * C
    for j in range(N):
        clean_cut = 0
        cut = log[j] // i
        if log[j] % i == 0:
            clean_cut = 1
        cost = i * cut * W - (cut - clean_cut) * C

        if cost > 0:
            temp_cost += cost
    if max_price < temp_cost:
        max_price = temp_cost

print(max_price)