# S3 solved

while True:
    try:
        a = int(input())
        if a == 1:
            print(1)
            continue
        base = 1
        n = 1
        while n != 0:
            n *= 10
            n += 1
            n %= a
            base += 1
        print(base)
    except:
        break