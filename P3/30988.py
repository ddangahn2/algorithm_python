# P3 런타임에러(ModuleNotFoundError)
import sympy as sp

n = int(input())
a_list = list(map(int, input().split()))

# f(x) = a(n) x^n + a(n-1) x^n-1 ... a(1) x + a(0)
# g(g(x)) = f(x) -> exist?
# g(x) = b(m) x^m + b(m-1) x^m-1 ... b(1) x + b(0)

# sympy를 사용하자.
x, fx, gx, gxgx = sp.symbols('x fx gx gxgx')
b0, b1, b2, b3, b4, b5 = sp.symbols('b0 b1 b2 b3 b4 b5')
fx = 0
gx = 0
gxgx = 0

exp_fx = n

# f(x) 만들기
for i in range(n + 1):
    fx += a_list[i]*x**exp_fx
    exp_fx -= 1

# root_n 찾기
if n in [1,4,9,16,25]:
    root_n = int(n ** (1/2))

    # g(x) 만들기
    exp_gx = root_n
    for i in range(root_n + 1):
        gx += sp.symbols('b{}'.format(i))*x**exp_gx
        exp_gx -= 1

    # g(g(x)) 만들기
    exp_gxgx = root_n
    for i in range(root_n + 1):
        gxgx += sp.symbols('b{}'.format(i))*gx**exp_gxgx
        exp_gxgx -= 1
    gxgx = sp.expand(gxgx)
    
    # f(x) == g(g(x)) x 계수에 따른 방정식 세우기
    equations = []
    for i in range(n, -1, -1):
        fx_degree = fx.coeff(x, i)
        gxgx_degree = gxgx.coeff(x, i)
        
        equation = sp.Eq(fx_degree, gxgx_degree)
        equations.append(equation)
    
    # 방정식 풀어서 계수 찾기
    b_list = sp.symbols('b0 b1 b2 b3 b4 b5')[:root_n+1]
    solution = sp.solve(equations, b_list)

    if solution != []:
        print(root_n)
        for i in range(root_n + 1):
            print(solution[0][i], end=' ')
    else:
        print(-1)
else:
    print(-1)