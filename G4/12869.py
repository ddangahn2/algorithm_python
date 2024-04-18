# G4 solved
# [1000 - 다이나믹 프로그래밍 2](https://www.acmicpc.net/workbook/view/3996)

from collections import deque
from itertools import permutations

N = int(input())
scv = list(map(int, input().split()))

while len(scv) != 3:
    scv.append(0)

dp = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 0

q = deque()
q.append([scv[0], scv[1], scv[2]])

while q:
    popq = q.popleft()

    if popq[0] == 0 and popq[1] == 0 and popq[2] == 0:
        print(dp[popq[0]][popq[1]][popq[2]])
        break
    for i in permutations([9,3,1], 3):
        curq = [max(popq[0] - i[0], 0), max(popq[1] - i[1], 0), max(popq[2] - i[2], 0)]
        curq.sort(reverse=True)
        
        if dp[curq[0]][curq[1]][curq[2]] == -1:
            dp[curq[0]][curq[1]][curq[2]] = dp[popq[0]][popq[1]][popq[2]] + 1
            q.append(curq)