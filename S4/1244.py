# S4

import sys
input = sys.stdin.readline

light_len = int(input())
light = list(map(int, input().split()))
N = int(input())


for _ in range(N):
    sex, num = map(int, input().split())
    
    # 남
    if sex == 1:
        i = 1
        while i * num <= light_len:
            light[i*num - 1] = 1 - light[i*num - 1]
            i += 1
    # 여
    if sex == 2:
        light[num-1] = 1 - light[num-1]
        left = num-2
        right = num

        while 0 <= left and right < light_len and light[left] == light[right]:
            light[left] = 1 - light[left]
            light[right] = 1 - light[right]
            left -= 1
            right += 1  

for i in range(1, light_len+1):
    print(light[i], end = " ")
    if i % 20 == 0 :
        print()