# G1 solved

N, K = map(int, input().split())
prime = 1000000007

#  N! / (K! * (N-K)!)
# 1000000007은 10억을 넘는 가장 작은 소수
# 페르마의 소정리에 의해서 a^p = a (mod p) a 정수, p 소수
# a^(p-2) = a^(-1) (mod p)
# N! / (K! * (N-K)!) = N! * (K! * (N-K)!)^(p-2)


def factorial(f):
    val = 1
    for i in range(2, f+1):
        val *= i
        val %= prime
    return val

def pow(value, power):
    if power == 0:
        return 1
    elif power == 1:
        return value
    
    result = pow(value, power // 2)
    if power % 2 == 0:
        return result * result % prime
    else:
        return result * result * value % prime

fact_n = int(factorial(N))
fact_k = int(factorial(K))
fact_n_minus_k = int(factorial(N-K))

answer = fact_n * pow(fact_k * fact_n_minus_k, prime-2) % prime

print(answer)