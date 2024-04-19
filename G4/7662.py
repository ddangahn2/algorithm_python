# G4 solved

import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    max_heap = []
    min_heap = []
    dict_heap = {}
    for k in range(K):
        DI, n = input().strip().split()
        n = int(n)

        if DI == "D":
            # 최대값 삭제
            if n == 1:
                if dict_heap != {}:
                    pop = heapq.heappop(max_heap)
                    while -pop not in dict_heap:
                        pop = heapq.heappop(max_heap)
                    dict_heap[-pop] -= 1
                    if dict_heap[-pop] == 0:
                        dict_heap.pop(-pop)
            # 최소값 삭제
            elif n == -1:
                if dict_heap != {}:
                    pop = heapq.heappop(min_heap)
                    while pop not in dict_heap:
                        pop = heapq.heappop(min_heap)
                    dict_heap[pop] -= 1
                    if dict_heap[pop] == 0:
                        dict_heap.pop(pop)
        elif DI == "I":
            if n in dict_heap:
                dict_heap[n] += 1
            else:
                dict_heap[n] = 1
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
    if dict_heap == {}:
        print("EMPTY")
    else:
        max_pop = heapq.heappop(max_heap)
        while -max_pop not in dict_heap:
            max_pop = heapq.heappop(max_heap)
        min_pop = heapq.heappop(min_heap)
        while min_pop not in dict_heap:
            min_pop = heapq.heappop(min_heap)
        print(-max_pop, end=' ')
        print(min_pop)