# G4 solved

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())


def bipartite_graph(node, group):
    # 0이 그룹1, 1이 그룹2, -1이 미방문
    global node_group
    
    node_group[node] = group

    for adj in graph[node]:
        if node_group[adj] == -1:
            if not bipartite_graph(adj, 1 - group):
                return False
        elif node_group[adj] == group:
            return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    node_group = [-1 for _ in range(V)]

    flag = 0
    for i in range(V):
        if node_group[i] == -1:
            if not bipartite_graph(i, 0):
                print("NO")
                flag = 1
                break
    if not flag:
        print("YES")