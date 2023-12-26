N = int(input())


def factorial(F):
    if F == 0:
        return 1
    return factorial(F - 1) * F

for i in range(N):
    L, R = map(int, input().split())
    print(int(factorial(R) / (factorial(L) * factorial(R-L))))