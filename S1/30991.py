# S1 solved

# E(x) = e^x
# S(x) = sinx, S'(x) = cosx
# C(x) = cosx, C'(x) = -sixx

# ESC(x) = e^x sinx cosx
# ESC'(x) = e^x sinx cosx + e^x cosx cosx - e^x sinx sinx
# ESC(n-1)(x) = a(n-1) e^x sinx cosx + b(n-1) e^x cosx cosx + c(n-1) e^x sinx sinx
# ESC(n)(x) = a(n) e^x sinx cosx + b(n) e^x cosx cosx + c(n) e^x sinx sinx

# a(n) = a(n-1) - 2 * b(n-1) + 2 * c(n-1)
# b(n) = a(n-1) + b(n-1)
# c(n) = -a(n-1) + c(n-1)

a = [1]
b = [1]
c = [-1]

n = int(input())

for i in range(n-1):
    new_a = a[-1] - 2*b[-1] + 2*c[-1]
    new_b = a[-1] + b[-1]
    new_c = -a[-1] + c[-1]

    a.append(new_a)
    b.append(new_b)
    c.append(new_c)

print(a[-1] + b[-1] + c[-1])