# S4 solved

N = int(input())

if N % 5 == 0:
    print(N//5)
elif ((N-3) % 5) == 0:
    print((N-3)//5 + 1)
elif ((N-6) % 5) == 0:
    print((N-6)//5 + 2)
elif N >= 9 and ((N-9) % 5) == 0:
    print((N-9)//5 + 3)
elif N >= 12 and ((N-12) % 5) == 0:
    print((N-12)//5 + 4)
else:
    print(-1)