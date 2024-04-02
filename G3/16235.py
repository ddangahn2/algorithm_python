# G3 solved
# [삼성 SW 역량 테스트 기출 문제](https://www.acmicpc.net/workbook/view/1152)

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

remain = [[5 for _ in range(N)] for _ in range(N)]
food = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
prop_tree = []

x_d = [-1,-1,-1,0,0,1,1,1]
y_d = [-1,0,1,-1,1,-1,0,1]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for i in range(N):
    for j in range(N):
        tree[i][j].sort()
        tree[i][j] = deque(tree[i][j])

def spring():
    for i in range(N):
        for j in range(N):
            dead = 0
            grown = deque()
            for k in tree[i][j]:
                if remain[i][j] >= k:
                    remain[i][j] -= k
                    grown.append(k+1)
                    if (k+1) % 5 == 0:
                        prop_tree.append((i,j))
                else:
                    dead += k//2
            tree[i][j] = grown
            # summer
            remain[i][j] += dead

def fall():
    global prop_tree
    for i, j in prop_tree:
        for dir in range(8):
            if 0 <= i + x_d[dir] < N and 0 <= j + y_d[dir] < N:
                tree[i + x_d[dir]][j + y_d[dir]].appendleft(1)
    prop_tree = []

def winter():
    for i in range(N):
        for j in range(N):
            remain[i][j] += food[i][j]

def ans():
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(tree[i][j])
    return answer

def printree(time):
    print(time+1)
    for i in range(N):
        for j in range(N):
            print(tree[i][j], end=' ')
            print(remain[i][j], end=' ')
        print()
    print()

for _ in range(K):
    spring()
    fall()
    winter()

print(ans())