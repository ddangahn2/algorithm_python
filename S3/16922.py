# S3 solved

from itertools import combinations_with_replacement

N = int(input())
res = set()
num = [1,5,10,50]

for temp in combinations_with_replacement(num, N):
    sum = 0
    for i in temp:
        sum += i
    res.add(sum)

print(len(res))