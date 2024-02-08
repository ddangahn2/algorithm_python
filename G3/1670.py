# G3

N = int(input())

store = {
    0 : 1,
    2 : 1,
    4 : 2,
}

def count(N):
    if N in store:
        return store[N]
    else:
        temp = 0
        if N % 4 == 0:
            for i in range(N//2, N-1, 2):
                temp += 2 * (count(i) * count(N-2-i))
                temp %= 987654321
        else:
            temp += count(N//2 - 1) * count(N//2 - 1)
            temp %= 987654321
            for i in range(N//2+1, N-1, 2):
                temp += 2 * (count(i) * count(N-2-i))
                temp %= 987654321
        store[N] = temp
        return temp

if N == 0:
    print(0)
else:
    print(count(N))
