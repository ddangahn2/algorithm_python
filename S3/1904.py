# S3 solved

#  F(n) = F(n-1) + F(n-2)

import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    exit(0)
elif N == 2:
    print(2)
    exit(0)

a = 1
b = 1
c = a + b
for i in range(3, N+1):
    a = b
    b = c
    c = a + b
    c %= 15746
print(c)