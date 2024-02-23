# S3 solved

import sys
input = sys.stdin.readline

while True:
    string = input().strip()

    if string == "*":
        break

    flag = 0
    for i in range(1, len(string)):
        d_set = set()
        for j in range(len(string) - i):
            d_set.add(string[j] + string[j+i])

        if len(d_set) != len(string) - i:
            flag = 1
            break
    
    if flag:
        print(f"{string} is NOT surprising.")
    else:
        print(f"{string} is surprising.")
