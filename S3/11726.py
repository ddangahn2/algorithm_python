# S3 solved

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    a = 1
    b = 2
    c = a + b

    for i in range(N-3):
        a = b
        b = c
        c = (a+b) % 10007
    print(c)
