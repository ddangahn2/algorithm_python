# G1 solved

N = int(input())
k = int(input())

st, ed = 1, k
ans = 0

while st <= ed:
    md = (st + ed) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(md//i, N)
    
    if temp >= k:
        ans = md
        ed = md - 1
    else:
        st = md + 1
print(ans)