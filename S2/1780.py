# S2 solved

n = int(input())

tmap = [list(map(int, input().split())) for _ in range(n)]

paper_minus = 0
paper_zero = 0
paper_plus = 0

def same_paper(x, y, paper_n):
    global paper_minus, paper_zero, paper_plus

    temp = tmap[x][y]
    paper_n_div = paper_n // 3

    if paper_n == 1:
        if temp == 0:
            paper_zero += 1
        elif temp == 1:
            paper_plus += 1
        else:
            paper_minus += 1
        return

    same_count = 0

    for i in range(paper_n):
        for j in range(paper_n):
            temp_x = x + i
            temp_y = y + j
            if temp != tmap[temp_x][temp_y]:
                same_paper(x, y, paper_n_div)
                same_paper(x, y + paper_n_div, paper_n_div)
                same_paper(x, y + paper_n_div * 2, paper_n_div)

                same_paper(x + paper_n_div, y, paper_n_div)
                same_paper(x + paper_n_div, y + paper_n_div, paper_n_div)
                same_paper(x + paper_n_div, y + paper_n_div * 2, paper_n_div)

                same_paper(x + paper_n_div * 2, y, paper_n_div)
                same_paper(x + paper_n_div * 2, y + paper_n_div, paper_n_div)
                same_paper(x + paper_n_div * 2, y + paper_n_div * 2, paper_n_div)
                return
    if temp == 0:
        paper_zero += 1
    elif temp == 1:
        paper_plus += 1
    else:
        paper_minus += 1

same_paper(0, 0, n)

print(paper_minus)
print(paper_zero)
print(paper_plus)


# 다른풀이. 아래 풀이가 시간이 더 적게 걸린다.

# import sys

# input = sys.stdin.readline

# result = [0, 0, 0]


# def tree(startX, startY, size):
#     flag = arr[startY][startX]
#     if size==1:
#         result[flag + 1] += 1
#         return

#     for i in range(size):
#         for j in range(size):
#             if arr[startY + i][startX + j] != flag:
#                 size //= 3
#                 tree(startX, startY, size)
#                 tree(startX + size, startY, size)
#                 tree(startX + size*2, startY, size)

#                 tree(startX, startY + size, size)
#                 tree(startX, startY + size*2, size)

#                 tree(startX+size, startY + size*2, size)
#                 tree(startX+size*2, startY + size, size)

#                 tree(startX + size, startY + size, size)
#                 tree(startX + size*2, startY + size*2, size)
#                 return
#     result[flag + 1] += 1


# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# tree(0,0,N)

# for i in result:
#     print(i)