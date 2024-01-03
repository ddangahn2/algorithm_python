# P5 solved

# 백조위치 기억해서 백조 위치부터 탐색해서 다른 백조와 만나는지 확인
# 안되면 호수 녹기 시작

from collections import deque

R, C = map(int,input().split())

day = 0


# 상하좌우
x = (0,0,-1,1)
y = (-1,1,0,0)

lake = [list(input()) for _ in range(R)]

swan_visited = [[False] * C for _ in range(R)]
water_visited = [[False] * C for _ in range(R)]

swan_visit = deque()
swan_next_visit = deque()

water_visit = deque()
water_next_visit = deque()

find_swan_r = 0
find_swan_c = 0

def lake_melt():
    while water_visit:
        r, c = water_visit.popleft()
        lake[r][c] = "."

        for dir in range(4):
            nr = r + y[dir]
            nc = c + x[dir]
            if 0 <= nr < R and 0 <= nc < C and not water_visited[nr][nc]:
                if lake[nr][nc] == "X":
                    water_next_visit.append((nr, nc))
                water_visited[nr][nc] = True

def swan_move():
    while swan_visit:
        r, c = swan_visit.popleft()

        if r == find_swan_r and c == find_swan_c:
            return True
        
        for dir in range(4):
            nr = r + y[dir]
            nc = c + x[dir]
            if 0 <= nr < R and 0 <= nc < C and not swan_visited[nr][nc]:
                if lake[nr][nc] == ".":
                    swan_visit.append((nr, nc))
                elif lake[nr][nc] == "X":
                    swan_next_visit.append((nr, nc))
                swan_visited[nr][nc] = True
    return False

for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            if not swan_visit:
                swan_visited[i][j] = True
                swan_visit.append((i, j))
            else:
                find_swan_r = i
                find_swan_c = j
            lake[i][j] = '.'
            water_visit.append((i, j))
            water_visited[i][j] = True
        elif lake[i][j] == ".":
            water_visit.append((i, j))
            water_visited[i][j] = True


while True:
    lake_melt()
    if swan_move():
        break
    
    swan_visit = swan_next_visit
    water_visit = water_next_visit

    swan_next_visit = deque()
    water_next_visit = deque()

    day += 1
print(day)