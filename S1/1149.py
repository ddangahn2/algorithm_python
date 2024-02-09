# S1 solved

import sys
input = sys.stdin.readline

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

Rmin = 0
Gmin = 0
Bmin = 0

for r, g, b in RGB:
    tpRmin = min(Gmin + r, Bmin + r)
    tpGmin = min(Rmin + g, Bmin + g)
    tpBmin = min(Rmin + b, Gmin + b)

    Rmin = tpRmin
    Gmin = tpGmin
    Bmin = tpBmin

print(min(Rmin, Gmin, Bmin))