# G1 solved

# 외판원 문제
from collections import deque
from itertools import permutations

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    room = [list(input()) for _ in range(h)]

    x = [-1,1,0,0]
    y = [0,0,-1,1]

    dirty_count = 0
    dirty_list = []
    dirty_distance = {}

    start_pos_row = 0
    start_pos_col = 0

    for row in range(h):
        for col in range(w):
            # 모든 경로를 지나야하니까 시작점도 더러운점이라고 본다
            if room[row][col] == 'o':
                start_pos_row = row
                start_pos_col = col
                dirty_count += 1
            elif room[row][col] == '*':
                dirty_list.append((row, col))
                dirty_count += 1
    dirty_list = [(start_pos_row, start_pos_col)] + dirty_list

    def bfs_find_distance(start_row, start_col):
        # 시작 위치에서 bfs해서 모든 먼지까지의 거리 파악
        q = deque()
        q.append((start_row, start_col))
        distance = [[0 for _ in range(w)] for _ in range(h)]
        cur_index = dirty_list.index((start_row, start_col))

        while q:
            row, col = q.popleft()

            for dir in range(4):
                new_row = row + x[dir]
                new_col = col + y[dir]

                if 0 <= new_row < h and 0 <= new_col < w and distance[new_row][new_col] == 0 and room[new_row][new_col] != 'x':
                    q.append((new_row, new_col))
                    distance[new_row][new_col] = distance[row][col] + 1
                    if room[new_row][new_col] == '*' and (start_row, start_col) != (new_row, new_col):
                        # 두 점 사이 거리를 저장한다. how?
                        # 이후 시작점과의 거리까지 저장해야한다.
                        # 어차피 모든 경로를 지나야하니까 시작점도 같이 보관하자
                        new_index = dirty_list.index((new_row, new_col))
                        if cur_index < new_index:
                            dirty_distance[(cur_index, new_index)] = distance[new_row][new_col]
                        else:
                            dirty_distance[(new_index, cur_index)] = distance[new_row][new_col]

    # 그래프 완성
    for dirty in dirty_list:
        bfs_find_distance(dirty[0], dirty[1])

    # 만약 도달할 수 없는점 있다면 break
    if len(dirty_distance) != (dirty_count * (dirty_count-1) / 2):
        print(-1)
        continue

    # 모든 경로를 지나면서 비용이 최소인 경로 찾기
    nodes = [i for i in range(1, len(dirty_list))]
    all_routes = list(permutations(nodes))
    min_cost = float('inf')

    for route in all_routes:
        cost = dirty_distance[(0, route[0])]
        for i in range(len(route)-1):
            min_route = min(route[i], route[i+1])
            max_route = max(route[i], route[i+1])
            cost += dirty_distance[(min_route, max_route)]
        min_cost = min(min_cost, cost)

    print(min_cost)