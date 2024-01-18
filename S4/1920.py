# S4 solved

N = int(input())
ListN = list(map(int, input().split()))

Map = {}

for i in ListN:
    Map[i] = 0

M = int(input())
ListM = list(map(int, input().split()))

for i in ListM:
    if i in Map:
        print(1)
    else:
        print(0)