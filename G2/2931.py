# G2 solved

# M과 Z위치 찾기
# 가스흐름이 유일하므로 M과 Z 주위에 연결된 파이프는 1개
# 파이프 따라 가보면 빈 위치가 보인다
# 빈 위치 주위로 파이프 뚫린 위치를 파악한다.

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

pipe = [list(input().strip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

Mrow = Mcol = Zrow = Zcol = 0

# 상,하, 좌,우
x = [-1,1,0,0]
y = [0,0,-1,1]

# 상, 하, 좌, 우에 연결되는 파이프
connect = [
    ['|', '+', '1', '4'],
    ['|', '+', '2', '3'],
    ['-', '+', '1', '2'],
    ['-', '+', '3', '4'],
]

pipemap = {
    '|' : (0, 1),
    '-' : (2, 3),
    '+' : (0, 1, 2, 3),
    '1' : (1, 3),
    '2' : (0, 3),
    '3' : (0, 2),
    '4' : (1, 2)
}
rev_pipemap = {v:k for k,v in pipemap.items()}

# M과 Z위치 찾기
for i in range(R):
    for j in range(C):
        if pipe[i][j] == 'M':
            Mrow = i
            Mcol = j
        elif pipe[i][j] == 'Z':
            Zrow = i
            Zcol = j

visited[Mrow][Mcol] = True
visited[Zrow][Zcol] = True

# 가스흐름이 유일하므로 M과 Z 주위에 연결된 파이프는 1개
for dir in range(4):
    if 0 <= Mrow + x[dir] < R and 0 <= Mcol + y[dir] < C and pipe[Mrow + x[dir]][Mcol + y[dir]] in connect[dir]:
        Mrow += x[dir]
        Mcol += y[dir]
        break
for dir in range(4):
    if 0 <= Zrow + x[dir] < R and 0 <= Zcol + y[dir] < C and pipe[Zrow + x[dir]][Zcol + y[dir]] in connect[dir]:
        Zrow += x[dir]
        Zcol += y[dir]
        break

visited[Mrow][Mcol] = True
visited[Zrow][Zcol] = True

# 파이프 따라 가보면 빈 위치가 보인다
# 추가로 파이프가 나오지 못하는 위치를 파악하면 된다.
q = deque()
q.append((Mrow, Mcol))
q.append((Zrow, Zcol))

Brow = 0
Bcol = 0

while q:
    r, c = q.popleft()

    for dir in pipemap[pipe[r][c]]:
        nr = r + x[dir]
        nc = c + y[dir]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            visited[nr][nc] = True

            if pipe[nr][nc] in connect[dir]:
                q.append((nr, nc))
            else:
                Brow = nr
                Bcol = nc
print(Brow + 1, Bcol + 1, end=' ')

# 빈 위치 주위로 파이프 뚫린 위치를 파악한다.
Bconnect = []

for dir in range(4):
    if 0 <= Brow + x[dir] < R and 0 <= Bcol + y[dir] < C and pipe[Brow + x[dir]][Bcol + y[dir]] in connect[dir]:
        Bconnect.append(dir)

print(rev_pipemap[tuple(Bconnect)])