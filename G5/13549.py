# G5 solved

from collections import deque

n, k = map(int, input().split())

h = [-1] * 200003

q = deque()
q.append(n)
next_q = deque()

h[n] = 0

def value_change(pos, val):
    if h[pos] < 0:
        h[pos] = val
        return True
    else:
        if h[pos] > val:
            h[pos] = val
            return True
        else:
            return False

def find():
    while q:
        pos = q.popleft()
        temp = h[pos]
        
        if pos == k:
            return 0
        
        if 0 <= 2 * pos <= 2 * k:
            if value_change(2 * pos, temp):
                next_q.appendleft(2 * pos)
        
        if 0 <= pos + 1 <= k:
            if value_change(pos + 1, temp + 1):
                next_q.append(pos + 1)

        if 0 <= pos - 1 <= 100000:
            if value_change(pos - 1, temp + 1):
                next_q.append(pos - 1)
    return 1

while find():
    q = next_q
    next_q = deque()

print(h[k])