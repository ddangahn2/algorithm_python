# S4 solved

N = int(input())

cnt = 0
Ntemp = N
while Ntemp != 1:
    Ntemp //= 2
    cnt += 1

twos = 2 ** cnt
last = 0

if N == twos:
    print(N)
else:
    print(2 * (N - twos))