# G5 solved

from collections import deque

M, N = map(int,input().split())

box = [list(map(int, input().split())) for _ in range(N)]

good_tomato = deque()
next_good_tomato = deque()

not_good_tomato_count = 0

x = [-1,1,0,0]
y = [0,0,-1,1]
day = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            good_tomato.append((i,j))
        elif box[i][j] == 0:
            not_good_tomato_count+=1

def all_tomato_good():
    global day, not_good_tomato_count
    temp = not_good_tomato_count
    while good_tomato:
        r, c = good_tomato.popleft()
        for dir in range(4):
            nr = r + x[dir]
            nc = c + y[dir]

            if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
                box[nr][nc] = 1
                not_good_tomato_count -= 1
                next_good_tomato.append((nr, nc))
    day += 1
    if temp == not_good_tomato_count:
        day -= 1
        return 0
    return 1

while True:
    result = all_tomato_good()
    good_tomato = next_good_tomato
    next_good_tomato = deque()
    
    if not_good_tomato_count == 0:
        print(day)
        break
    elif result == 0 and not_good_tomato_count != 0:
        print(-1)
        break