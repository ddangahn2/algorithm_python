# G3 solved

N = int(input())

prime_list = [True] * 4_000_001
prime_list[0] = prime_list[1] = False

for i in range(2, 2_000_001):
    if prime_list[i] == True:
        j = 2
        while i * j < 4_000_001:
            prime_list[i * j] = False
            j += 1

prime = []
for i in range(4_000_001):
    if prime_list[i] == True:
        prime.append(i)
st = 0
ed = 0
# st ~ ed까지 더하기
# 부족하면 ed 추가
# 넘치면 st 뺴기
count = 0
check = 2
while st <= ed:
    if check == N:
        count += 1
        check -= prime[st]
        st += 1
    elif check < N:
        ed += 1
        if ed == len(prime):
            break
        check += prime[ed]
    else:
        check -= prime[st]
        st += 1

print(count)