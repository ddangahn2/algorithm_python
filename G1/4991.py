
from collections import deque

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    board = [list(input()) for _ in range(h)]

    x = [-1,1,0,0]
    y = [0,0,-1,1]

    move = 0
    finish = 0

    def how_many_dirty():
        dirty = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == "o":
                    start = (i, j)
                if board[i][j] == "*":
                    dirty += 1
        return start, dirty

    def bfs(r, c, dirty):
        global move, finish
        q = deque()
        q.append((r, c))
        visited = [[-1 for _ in range(w)] for _ in range(h)]
        visited[r][c] = 0

        if dirty == 0:
            finish = 1

        while q:
            r, c = q.popleft()
            
            for i in range(4):
                nr = r + x[i]
                nc = c + y[i]
                if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == -1 and board[nr][nc] != "x":
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                    if board[nr][nc] == "*":
                        board[nr][nc] = "."
                        move += visited[nr][nc]
                        bfs(nr, nc, dirty - 1)
                        return
        

    # dirty 개수 세기
    start, dirty = how_many_dirty()
    bfs(start[0], start[1], dirty)

    if finish == 0:
        print(-1)
    else:
        print(move)