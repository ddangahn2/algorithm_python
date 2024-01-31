# G5 solved

N, P, Q = map(int, input().split())

memo = {}

def divide(value):
    if value == 0:
        return 1
    elif value == 1:
        return 2
    Pvalue = value // P
    Qvalue = value // Q
    if Pvalue in memo and Qvalue in memo:
        return memo[Pvalue] + memo[Qvalue]
    else:
        PQvalue = divide(Pvalue) + divide(Qvalue)
        memo[value] = PQvalue
        return PQvalue

if N == 0:
    print(1)
elif N == 1:
    print(2)
else:
    print(divide(N))