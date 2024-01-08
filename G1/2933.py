# G1 solved

from collections import deque

r, c = map(int, input().split())

cave = [list(input()) for _ in range(r)]

n = int(input())

bars = [r - x for x in list(map(int, input().split()))]

x = [-1,1,0,0]
y = [0,0,-1,1]

# 왼->오, 오->왼 ...

# 막대 던짐
# 클러스터 분리 여부 확인 (how?) 및 클러스터 확인

# 클러스터가 떨어질 때, 클러스터 각 열의 맨 아래 부분중 하나가 바닥 또는 미네랄 위로 떨어질 떄 멈춤

def throw_bar(bar_row, dir):
    l2r = (dir % 2)
    
    for i in range(c):
        # i = 0, l2r = 0 index = 0
        # i = 0, l2r = 1 index = -1
        # i = 1, l2r = 0 index = 1
        # i = 1, l2r = 1 index = -2
        bar_col = pow(-1, l2r) * (i + l2r)
        if cave[bar_row][bar_col] == 'x':
            cave[bar_row][bar_col] = '.'
            return bar_row, bar_col

def cave_ground():
    ground = []
    for i in range(c):
        if cave[r-1][i] == 'x':
            cave[r-1][i] = 'o'
            ground.append(i)
    return ground

def bfs(minerals):
    q = deque()

    base_cluster = []

    for mineral in minerals:
        q.append((r-1, mineral))
        
    while q:
        row, col = q.popleft()
        base_cluster.append((row, col))

        for dir in range(4):
            n_row = row + x[dir]
            n_col = col + y[dir]

            if 0 <= n_row < r and 0 <= n_col < c and cave[n_row][n_col] == 'x':
                cave[n_row][n_col] = 'o'
                q.append((n_row, n_col))
    return base_cluster

# 클러스터가 있으면 클러스터의 모든 끝점 확인
def cluster_bottom():
    clusters = []
    cluster_btm = {}
    for i in range(r):
        for j in range(c):
            if cave[i][j] == "x":
                clusters.append((i,j))
                # 현 시점이 항상 가장 아래쪽이다
                cluster_btm[j] = i

    return cluster_btm, clusters

# 끝점이 아래로 얼마나 떨어지는지 체크
def cluster_fall(cluster_btm, clusters, base_clusters):
    fall = r
    for col, row in cluster_btm.items():
        for fall_r in range(row + 1, r, 1):
            if cave[fall_r][col] == 'o':
                fall = min(fall, fall_r - row - 1)
                break
            fall = min(fall, r - row - 1)

    clusters.reverse()
    for row, col in clusters:
        cave[row + fall][col] = 'x'
        cave[row][col] = '.'
    
    for row, col in base_clusters:
        cave[row][col] = 'x'


for index, bar in enumerate(bars, start=0):
    throw_bar(bar, index)

    base_clusters = bfs(cave_ground())
    cluster_btm, clusters = cluster_bottom()

    cluster_fall(cluster_btm, clusters, base_clusters)

for cav in cave:
    for ca in cav:
        print(ca, end='')
    print()