# S1 solved
# [대기업 코테에서 나오는 유형 모음](https://www.acmicpc.net/workbook/view/8708)

string = list(input())

count_b = 0

for i in string:
    if i == "b":
        count_b += 1

max_b = string[:count_b].count("b")
temp_b = max_b

st = 0
ed = count_b
for i in range(len(string)):
    if string[st] == "b":
        temp_b -= 1
    st += 1
    st %= len(string)

    ed %= len(string)
    if string[ed] == "b":
        temp_b += 1
    ed += 1
    
    max_b = max(max_b, temp_b)
print(count_b - max_b)