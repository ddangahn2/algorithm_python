# S2 solved

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in line:
        heapq.heappush(heap, j)
        if len(heap) > N:
            heapq.heappop(heap)

print(heapq.heappop(heap))