# G1 solved

import sys
from math import inf
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]
visited = [[K+1 for _ in range(M)] for _ in range(N)]
day = 1

x = [-1,1,0,0]
y = [0,0,-1,1]

# 모든 상태를 저장한다?
# 부순 벽 개수가 key point다
# 각 지점에서 부순 벽 개수가 같은 두 상태를 저장할 필요 없다
# 벽 통과시에는 무조건 밤이 된다.

visited[0][0] = 0

def bfs():
    global day
    q = deque()
    # r, c, dist, breaked_wall
    q.append((0, 0, 0))
    distmap = {1: q}
    while distmap:
        nq = distmap.pop(day, None)

        while nq:
            r, c, b = nq.popleft()

            if r == N-1 and c == M-1:
                return day

            for dir in range(4):
                nr = r + x[dir]
                nc = c + y[dir]

                bflag = 0
                dflag = 0
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] > b:
                    if board[nr][nc] == '1' and b < K:
                        bflag =  1
                        if day % 2 == 0:
                            dflag = 2
                        else:
                            dflag = 1
                    elif board[nr][nc] == '0':
                        dflag =  1
                    else:
                        continue
                    visited[nr][nc] = b + bflag
                    if day + dflag not in distmap:
                        distmap[day + dflag] = deque([(nr, nc, b + bflag)])
                    else:
                        distmap[day + dflag].append((nr, nc, b + bflag))  
        day += 1    
    return -1

print(bfs())