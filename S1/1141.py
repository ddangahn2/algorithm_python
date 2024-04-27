# S1 solved

import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

words.sort(key=lambda x: len(x))

has_prefix = 0
for i in range(N):
    for j in range(i+1,N):
        if words[i] == words[j][:len(words[i])]:
            has_prefix += 1
            break

print(N - has_prefix)