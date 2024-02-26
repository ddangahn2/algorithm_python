# G3 solved

import sys
input = sys.stdin.readline

N = int(input())
flower = []
for i in range(N):
    stm, std, edm, edd = map(int, input().split())
    if edm <= 2 or (edm == 3 and edd == 1) or stm == 12:
        continue
    flower.append([stm, std, edm, edd])

flower.sort(key = lambda x : (x[0],x[1],x[2],x[3]), reverse=True)

count = 0
maxedm = 3
maxedd = 1

def choose_flower(maxedm, maxedd):
    tpedm = maxedm
    tpedd = maxedd
    while flower:
        stm, std, edm, edd = flower.pop()
        if stm <= (maxedm-1) or (stm == maxedm and std <= maxedd):
            if edm > tpedm or (edm == tpedm and edd > tpedd):
                tpedm = edm
                tpedd = edd
        else:
            flower.append([stm, std, edm, edd])
            return tpedm, tpedd
    return tpedm, tpedd

while True:
    count += 1
    tpedm, tpedd = choose_flower(maxedm, maxedd)
    if tpedm >= 12:
        print(count)
        break
    if tpedm == maxedm and tpedd == maxedd or flower == []:
        print(0)
        break
    maxedm = tpedm
    maxedd = tpedd