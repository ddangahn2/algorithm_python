# G4 solved

N = int(input())
A = [0] + list(map(int, input().split()))

backA = [(0,0) for _ in range(N+1)]

long = 0
last = 0

for i in range(N):
    for j in range(i+1,N+1):
        if A[j] > A[i] and backA[j][1] < backA[i][1] + 1:
            backA[j] = (i, backA[i][1] + 1)
            if backA[i][1] + 1 > long:
                long = backA[i][1] + 1
                last = j

back = []
while last != 0:
    back.append(A[last])
    last = backA[last][0]

print(long)
print(*back[::-1], end=' ')