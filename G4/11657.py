# G4 solved

import sys
import math
inf = math.inf
input = sys.stdin.readline

N, M = map(int, input().split())

bus = [list(map(int,input().split())) for _ in range(M)]

bellmanford = [inf for _ in range(N)]
bellmanford[0] = 0

negative_cycle = False

for i in range(N):
    for edge in bus:
        st, ed, time = edge
        st -= 1
        ed -= 1
        if i == N-1:
            if bellmanford[ed] > bellmanford[st] + time:
                negative_cycle = True
                break
        if bellmanford[ed] > bellmanford[st] + time:
            bellmanford[ed] = bellmanford[st] + time
        
  
if not negative_cycle:
    for i in range(1,N):
        if bellmanford[i] == inf:
            print(-1)
        else:
            print(bellmanford[i])
else:
    print(-1)