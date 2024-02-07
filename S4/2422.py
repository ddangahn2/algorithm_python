# S4 solved

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nocombo = [set() for _ in range(N)]

if N <= 2:
    print(0)
else:
    # 전체 경우수
    total = N * (N-1) * (N-2) // 6 - (N-2) * M

    nocount = 0
    for _ in range(M):
        a, b = map(int, input().split())
        # 빠지는 경우 수 (조합 2개에 나머지 1개)
        nocount += len(nocombo[a-1] | nocombo[b-1])
        nocombo[a-1].add(b)
        nocombo[b-1].add(a)
    print(total + nocount)