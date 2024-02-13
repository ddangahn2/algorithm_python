# S1 solved

from collections import deque
N, K = map(int, input().split())

Nmap = [-1 for _ in range(100_001)]

Nmap[N] = 0
ans = 0
q = deque()
q.append(N)
while q:
    qpop = q.popleft()
    t = Nmap[qpop]

    if K == qpop:
        ans = t
        break
    elif K in [qpop+1, qpop-1, qpop*2]:
        ans = t+1
        break

    if qpop + 1 <= 100_000 and Nmap[qpop+1] == -1:
        Nmap[qpop + 1] = t+1
        q.append(qpop+1)
    if 0 <= qpop - 1 and Nmap[qpop-1] == -1:
        Nmap[qpop - 1] = t+1
        q.append(qpop-1)
    if (qpop * 2) <= 100_000 and Nmap[qpop*2] == -1:
        Nmap[qpop * 2] = t+1
        q.append(qpop*2)
print(ans)