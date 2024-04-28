# S3 solved

import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
X = int(input())

answer = 0
left, right = 0, N-1
while left < right:
    temp = numbers[left] + numbers[right]
    if temp == X:
        answer += 1
        left += 1
    elif temp < X:
        left += 1
    else:
        right -= 1
print(answer)