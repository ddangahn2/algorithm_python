# G5 solved

N = int(input())
X = list(map(int, input().split()))
X.sort()
# 길이 len(X) * 2

S = [-1 for _ in range(len(X)*2)]
flag = 0
ans = []
def makeS(tempS, tempX):
    global flag
    if len(tempX) == 0:
        flag = 1
        ans.append(tempS)
        return
    else:
        temp = tempX.pop(0)
        for i in range(len(tempS) - temp - 1):
            if tempS[i] == -1 and tempS[i + temp + 1] == -1:
                temp2S = tempS[:]
                temp2S[i] = temp
                temp2S[i + temp + 1] = temp
                makeS(temp2S, tempX[:])


makeS(S, X)
if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in range(len(ans[0])):
        print(ans[0][i], end=' ')