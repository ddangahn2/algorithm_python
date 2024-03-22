# S4 solved

import sys
input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    s = input().strip()
    stack = []

    for i in range(len(s)):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if not stack:
        count += 1
print(count)