# G4 solved

from collections import deque
# N은 농장 너비
# K는 소의 수
# R은 길의 개수
N, K, R = map(int, input().split())

# 길의 정보 저장
row_link = [[False for _ in range(N-1)] for _ in range(N)]
col_link = [[False for _ in range(N)] for _ in range(N-1)]

x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

# 길의 개수만큼 길의 정보를 입력받는다
for i in range(R):
    r, c, r2, c2 = map(int, input().split())
    if r == r2:
        row_link[r-1][min(c,c2)-1] = True
    else:
        col_link[min(r,r2)-1][c-1] = True

# 소가 있는 위치를 저장할 리스트
cow = []
for i in range(K):
    cr, cc = map(int, input().split())
    cow.append((cr-1, cc-1))

# 소의 위치에서 bfs
    
def bfs(r, c):
    global count
    q = deque()
    q.append((r,c))
    tmap = [[False for _ in range(N)] for _ in range(N)]
    tmap[r][c] = True
    while q:
        r, c = q.popleft()

        for dir in [0,1]:
            nr = r + x[dir]
            nc = c + y[dir]
            if 0 <= nr < N and 0 <= nc < N and not tmap[nr][nc] and not row_link[min(r,nr)][min(c,nc)]:
                tmap[nr][nc] = True
                q.append((nr,nc))
        for dir in [2,3]:
            nr = r + x[dir]
            nc = c + y[dir]
            if 0 <= nr < N and 0 <= nc < N and not tmap[nr][nc] and not col_link[min(r,nr)][min(c,nc)]:
                tmap[nr][nc] = True
                q.append((nr,nc))
    for i in cow:
        if tmap[i[0]][i[1]] == False:
            count += 1

count = 0
for i in cow:
    bfs(i[0], i[1])

print(count // 2)