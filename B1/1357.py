# B1 solved

def Rev(x):
    return int(''.join(list(str(x))[::-1]))
    
X, Y = map(int, input().split())

print(Rev(Rev(X) + Rev(Y)))