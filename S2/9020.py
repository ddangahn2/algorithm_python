# S2 solved

import sys
input = sys.stdin.readline

N = [True] * 10_001
N[0] = N[1] = False
T = int(input())

for i in range(2, 5_000):
    if N[i] == False:
        continue
    j = 2
    while i * j <= 10_000:
        N[i*j] = False
        j += 1

for _ in range(T):
    n = int(input())
    for i in range(n//2, 1, -1):
        if N[i] and N[n-i]:
            print(i, n-i)
            break