# G5 solved

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = list(input())
    n = int(input())
    x = input()
    error = 0
    x = x.strip("[]\n")
    if x != "":
        x = list(map(int, x.split(",")))

    st = 0
    ed = n-1
    rv = 0

    for i in p:
        if i == 'R':
            rv = 1 - rv
        elif i == 'D':
            if rv == 0:
                st += 1
            else:
                ed -= 1

            if st - 1 > ed:
                error = 1
                break
    
    if error:
        print("error")
    else:
        if rv == 0:
            print("["+",".join(map(str, x[st:ed+1])) + "]")
        else:
            if st == 0:
                print("["+",".join(map(str, x[ed::-1])) + "]")
            else:
                print("["+",".join(map(str, x[ed:st-1:-1])) + "]")