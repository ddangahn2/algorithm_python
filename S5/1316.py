num = int(input())
result = 0

for i in range(num):
    a = input()
    dic = {}
    for char in enumerate(a):
        if(dic.get(char[1]) == None):
            dic[char[1]] = char[0]
        else:
            if(dic[char[1]] + 1 < char[0]):
                result += 1
                break
            else:
                dic[char[1]] = char[0]
print(num - result)