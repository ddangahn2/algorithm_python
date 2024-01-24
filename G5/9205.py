# G5 solved

t = int(input())

for _ in range(t):
    n = int(input())

    store = []
    house = list(map(int, input().split()))
    store.append(house)
    for _ in range(n):
        store.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    store.append(festival)

    # 1000미터 이내를 모두 그래프로 묶는다 (무향그래프)
    graph = {}
    for i in range(n+2):
        for j in range(i+1,n+2):
            if abs(store[i][0] - store[j][0]) + abs(store[i][1] - store[j][1]) <= 1000:
                if i not in graph:
                    graph[i] = [j]
                else:
                    graph[i].append(j)
                if j not in graph:
                    graph[j] = [i]
                else:
                    graph[j].append(i)
    
    # 그래프 탐색
    q = [0]
    visited = []
    found = 0
    
    while q:
        nq = q.pop()
        if nq == n+1:
            found = 1
            break
        if nq not in visited:
            visited.append(nq)
            if nq in graph:
                for nq_adj in graph[nq]:
                    if nq_adj not in visited:
                        q.append(nq_adj)

    if found == 0:
        print("sad")
    else:
        print("happy")