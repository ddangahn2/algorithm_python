# S1 solved
# [코딩 테스트 준비 - 기초](https://www.acmicpc.net/workbook/view/9370)

import sys
input = sys.stdin.readline

# 3 ~ 1_000_000까지의 소수 구하기
prime = []
p_check = [True] * 1_000_001

p_check[0] = p_check[1] = p_check[2] = False

for i in range(3, 1_000_001):
    if p_check[i] == True:
        prime.append(i)
        
        j = 2
        while i * j < 1_000_001:
            p_check[i * j] = False
            j += 1

while True:
    N = int(input())
    if N == 0:
        break
    flag = 1
    for i in prime:
        if p_check[N - i] == True:
            print(f"{N} = {i} + {N-i}")
            flag = 0
            break
    if flag == 1:
        print("Goldbach's conjecture is wrong.")