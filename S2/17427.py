# S2 solved
# [코딩 테스트 준비 - 기초](https://www.acmicpc.net/workbook/view/9370)

N = int(input())
ans = N

for i in range(2, N+1):
    ans += (N//i) * i

print(ans)