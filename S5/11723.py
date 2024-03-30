# S5 solved
# [대기업 코테에서 나오는 유형 모음](https://www.acmicpc.net/workbook/view/8708)

import sys
input = sys.stdin.readline

S = set()

M = int(input())
for _ in range(M):
    a = input().strip()
    
    if a == "all":
        S = {i for i in range(1, 21)}
    elif a == "empty":
        S = set()
    else:
        a, b = a.split()
        b = int(b)

        if a == "add":
            S.add(b)
        elif a == "remove":
            S.discard(b)
        elif a == "check":
            if b in S:
                sys.stdout.write("1\n")
            else:
                sys.stdout.write("0\n")
        elif a == "toggle":
            if b in S:
                S.discard(b)
            else:
                S.add(b)