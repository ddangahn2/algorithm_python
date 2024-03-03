# S3 solved

import sys
input = sys.stdin.readline

def cantor(st, ed):
    if st + 1 == ed:
        return
    else:
        div = (ed - st +1) // 3
        for i in range(st + div, st + 2 * div):
            cantor_list[i] = False
        cantor(st, st + div)
        cantor(st + div * 2, ed)

while True:
    try:
        N = int(input())
        cantor_list = [True] * (3**N)

        if N == 0:
            print("-")
        else:
            cantor(0, (3**N))
            for i in range(3**N):
                if cantor_list[i] == True:
                    print("-", end="")
                else:
                    print(" ", end="")
            print()
    except:
        break