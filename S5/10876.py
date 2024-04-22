# S5 solved

import sys
input = sys.stdin.readline

N = int(input())
L = set(map(int, input().split()))

for i in sorted(list(L)):
    print(i, end=' ')