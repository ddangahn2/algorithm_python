# G4 solved

N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]
house.sort()

ans = 0

def binary_search(st, ed):
    while st <= ed:
        mid = (st + ed) // 2
        cur = house[0]
        count = 1

        for i in range(1, len(house)):
            if house[i] >= cur + mid:
                count += 1
                cur = house[i]
        if count >= C:
            global ans
            st = mid + 1
            ans = mid
        else:
            ed = mid - 1

if C == 2:
    print(house[N-1] - house[0])
else:
    binary_search(1, house[-1] - house[0])
    print(ans)