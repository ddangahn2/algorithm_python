# S4 solved

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    stack = 0
    parentheses = list(input().strip())

    isVPS = 0
    for par in parentheses:
        if par == "(":
            stack += 1
        else:
            if stack == 0:
                isVPS = 1
                break
            else:
                stack -= 1
    if isVPS:
        print("NO")
    elif stack == 0:
        print("YES")
    else:
        print("NO")