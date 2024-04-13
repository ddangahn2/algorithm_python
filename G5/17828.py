# G5 solved

import sys
input = sys.stdin.readline

N, X = map(int, input().split())

if N > X or N * 26 < X:
    print("!")
else:
    array = ["A"] * N
    X -= N
    
    z_count = X//25
    z_left = X % 25

    i = N-1
    while z_count > 0:
        array[i] = "Z"
        i -= 1
        z_count -= 1
    if z_left > 0:
        array[i] = chr(z_left + 65)
    
    print("".join(array))