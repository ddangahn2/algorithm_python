# S1 solved

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vote = list(map(int, input().split()))

wall = []


def pushwall(index):
    while index >= 1:
        if wall[index][1] > wall[index-1][1]:
            wall[index], wall[index-1] = wall[index-1], wall[index]
            index -= 1
        else:
            break
    
def popwall():
    least = wall[-1][1]
    latest = 10000
    temp_index = 0
    for idx in range(len(wall)):
        if wall[idx][1] == least and latest > wall[idx][2]:
            latest = wall[idx][2]
            temp_index = idx
    wall.pop(temp_index)
            

for i, voted in enumerate(vote):
    flag = 0
    for idx in range(len(wall)):
        if wall[idx][0] == voted:
            flag = 1
            wall[idx][1] += 1
            pushwall(idx)
            break
    if not flag:
        if len(wall) < N:
            wall.append([voted, 1, i])
        else:
            popwall()
            wall.append([voted, 1, i])

for std in sorted([x[0] for x in wall]):
    print(std, end=' ')