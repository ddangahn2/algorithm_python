# G4 solved

import sys
from collections import deque
from itertools import combinations
from math import inf
input = sys.stdin.readline

# 초기조건
N = int(input())
people = list(map(int, input().split()))
tot_people = sum(people)
adj = {}
for idx in range(1, len(people)+1):
    adj_list = list(map(int, input().split()))
    for i in range(1, len(adj_list)):
        if idx not in adj:
            adj[idx] = [adj_list[i]]
        else:
            adj[idx].append(adj_list[i])

# 절반을 나눠서 combination set
combination_list = []
for i in range(1, (N//2) + 1):
    combination_list.extend(list(combinations([i for i in range(1, N+1)], i)))

# 나누어진 2개집합 갈수 있는지 확인
def has_path(path_list):
    if len(path_list) == 1:
        return True
    else:
        q = deque()
        q.append(path_list[0])
        visited = [path_list[0]]
        while q:
            nq = q.popleft()
            if nq in adj:
                for i in adj[nq]:
                    if i in path_list and i not in visited:
                        visited.append(i)
                        q.append(i)
        if set(path_list) == set(visited):
            return True
        return False

# 갈 수 있으면 인구 차이 계산
def how_many_people(part_list):
    count = 0
    for i in part_list:
        count += people[i-1]
    return count

minimum = inf
for part1 in combination_list:
    part2 = list(set([i for i in range(1, N+1)]) - set(part1))
    if has_path(part1) and has_path(part2):
        part1_count = how_many_people(part1)
        part2_count = tot_people - how_many_people(part1)

        minimum = min(abs(part1_count - part2_count), minimum)
if minimum == inf:
    print(-1)
else:
    print(minimum)