# G2 solved

# 피사노 주기 (?)
# 피보나치 수를 어떤 수로 나누게 될 경우 함상 주기를 가진다.
# 주기는 M = 10^k (k>2) 일 때, 15*10^(k-1) 이다.

# 1,000,000 으로 나눴으므로 주기는 15*10^5 이다. 

n = int(input())

pisano_period = 1500000
n = n % pisano_period

a = 0
b = 1
c = 1

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(n - 1):
        c = (a + b) % 1000000
        a = b
        b = c
    print(c)


# 주기를 모를 때
# 아래로 주기를 구할 수 있다.
# 아래는 0과 1이 다시 나오게 되는 주기를 구하는 식이고, 1,500,000 이 나온다.

# cnt = 1

# while True:
#     c = (a + b) % 1000000
#     a = b
#     b = c % 1000000
#     if b == 1 and a == 0:
#         break
#     else:
#         cnt += 1

# print(cnt)