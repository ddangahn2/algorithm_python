# S1 solved

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
T = list(map(int,input().split()))

start = max(T)
end = sum(T)

while start <= end:
    mid = (start + end) // 2 

    total = 0
    count = 1
    for t in T:
        if total + t > mid:
            count += 1
            total = 0
        total += t 

    if count <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
    
print(ans)