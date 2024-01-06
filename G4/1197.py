# G4 solved

# 프림
# 연결된 minnimum spanning tree 에서 최소 길이의 선만 연결한다(순환이 생기지 않게)

V, E = map(int, input().split())
edge_list = []

import heapq as hq

total_value = 0
node_edge = {}

for i in range(E):
    node1, node2, value = map(int, input().split())
    if node1 not in node_edge:
        node_edge[node1] = []
    if node2 not in node_edge:
        node_edge[node2] = []
    node_edge[node1].append([value, node2])
    node_edge[node2].append([value, node1])

# 1번부터
spanning_tree_hp = []
spanning_tree_node = set()
spanning_tree_node.add(1)

node = 1

while True:
    if len(spanning_tree_node) == V:
        print(total_value)
        break

    for i in node_edge[node]:
        value, new_node = i
        if new_node not in spanning_tree_node:
            hq.heappush(spanning_tree_hp, i)

    while spanning_tree_hp:
        value, new_node = hq.heappop(spanning_tree_hp)

        if new_node not in spanning_tree_node:
            spanning_tree_node.add(new_node)
            node = new_node
            total_value += value
            break