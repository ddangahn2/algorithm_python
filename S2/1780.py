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
