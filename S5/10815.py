# S5 solved
# [알고리즘 중급 1/3](https://www.acmicpc.net/workbook/view/3980)

# 상근 숫자카드 N개 정수 M개

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
find = list(map(int, input().split()))

# cards 이분탐색
def find_card(num):
    st = 0
    ed = len(cards)-1

    while st <= ed:
        md = (st + ed) // 2
        if cards[md] == num:
            return 1
        elif cards[md] < num:
            st = md + 1
        elif cards[md] > num:
            ed = md - 1
    return 0

for num in find:
    print(find_card(num), end=' ')