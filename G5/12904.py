# G5 solved

import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

flag = False
while T:
    if S == T:
        flag = True
        break
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T.reverse()

if flag:
    print(1)
else:
    print(0)