# G4 solved

string = list(input())
boom = list(input())
boom_len = len(boom)
# 문자열 포함시 부순다
# 붙인다
# 없을때까지

# 없애기 과정
stack = []
for i in string:
    stack.append(i)
    if len(stack) >= boom_len:
        if stack[len(stack) - boom_len : len(stack)] == boom:
            for j in range(boom_len):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))