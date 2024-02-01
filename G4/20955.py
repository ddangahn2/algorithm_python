# G4 런타임 에러 (RecursionError)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 전체 뉴런의 개수는 N-1개면 된다.
# 순환이 있다면 끊어주자.

# 순환을 어떻게 알고 끊지?
# 겹순환이 가능한가? 예를들어 하나의 뉴런을 끊을때 두개의 순환이 끊기는 경우
# 순환 생긴 개수만 파악하면 될것 같다.
answer = 0
circle = 0

synapses = [list(map(int, input().split())) for _ in range(M)]

edges = {}

for synapse in synapses:
    if synapse[0] not in edges:
        edges[synapse[0]] = [synapse[1]]
    else:
        edges[synapse[0]].append(synapse[1])
    if synapse[1] not in edges:
        edges[synapse[1]] = [synapse[0]]
    else:
        edges[synapse[1]].append(synapse[0])

nodes = ["w" for _ in range(N)]

def dfs(cur_node, pre_node):
    global circle
    if cur_node in edges:
        for cur_node_adj in edges[cur_node]:
            if nodes[cur_node_adj-1] == "w":
                nodes[cur_node_adj-1] = "g"
                dfs(cur_node_adj, cur_node)
                nodes[cur_node_adj-1] = "b"
            elif nodes[cur_node_adj-1] == "g" and cur_node_adj != pre_node:
                circle += 1

for i in range(N):
    if nodes[i] == "w":
        dfs(i+1, 0)

# 기존 순환을 끊는 횟수
answer += circle

# N-1은 트리가 되기 위해 필요한 가지 개수, M-circle은 기존 가지 수
answer += ((N - 1) - (M - circle))

print(answer)