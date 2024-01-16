# G4 solved

from collections import deque

N, K = map(int, input().split())

q = deque()
q.append((N,0))
visited = [-1] * 100001

while q:
    x, val = q.popleft()
    if x == K:
        print(val)
        break
    if 0 <= (x-1) <= 100_000 and visited[x-1] == -1:
        visited[x-1] = x
        q.append((x-1, val+1))
    if 0 <= (x+1) <= 100_000 and visited[x+1] == -1:
        visited[x+1] = x
        q.append((x+1, val+1))
    if 0 <= (2*x) <= 100_000 and visited[2*x] == -1:
        visited[2*x] = x
        q.append((2*x, val+1))

backtrack = []
path = K
while path != N:
    backtrack.append(path)
    path = visited[path]
backtrack.append(N)

print(' '.join(map(str, backtrack[::-1])))