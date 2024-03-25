# S5 solved

import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    total = 0
    max_height = 0
    temp_arr = []
    for i, height in enumerate(arr[1:]):
        if height > max_height:
            max_height = height
            temp_arr.append(height)
        else:
            for j in range(i):
                if temp_arr[j] > height:
                    total += i - j
                    temp_arr.insert(j, height)
                    break
    print(_+1, total)