#S5 solved

x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

# f(x) = ax^2 + bx + c
# g(x) = dx + e

# lazer_power = [F(x) - G(x)] x2 ~ x1

# F(x) = ax^3/3 + bx^2/2 + cx + C1
# G(x) = dx^2/2 + ex + C2

lazer_power_Fx = int(a * (x2 ** 3 - x1 ** 3) / 3 + b * (x2 ** 2 - x1 ** 2) / 2 + c * (x2 - x1))
lazer_power_Gx = int(d * (x2 ** 2 - x1 ** 2) / 2 + e * (x2 - x1))

lazer_power = lazer_power_Fx - lazer_power_Gx

print(lazer_power)