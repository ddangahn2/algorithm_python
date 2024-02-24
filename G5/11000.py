# G5 solved

import sys 
import heapq
input = sys.stdin.readline

N = int(input())

study = []
for i in range(N):
    st, ed = map(int, input().split())
    study.append([st, ed])
study.sort(key = lambda x : (x[0], x[1]))

# 끝나는시간
heap = [study[0][1]]
for i in range(1, N):
    if heap[0] <= study[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, study[i][1])

print(len(heap))