# G5 solved

# 아무문자 제거, 맨앞 1개 추가, 맨뒤 1개추가
ksa = input() # SA KSA
count = 0

Kksa = 0 # KSAKSA
Sksa = 0 # SAKSAK
Aksa = 0 # AKSAKS

if len(ksa) == 1:
    if ksa[0] != "K":
        print(2)
    else:
        print(0)
elif len(ksa) == 2:
    if ksa[0] == "K" and ksa[1] == "S":
        print(0)
    elif "K" in ksa or "S" in ksa:
        print(2)
    else:
        print(4)
else:
    for i in range(len(ksa)):
        if ksa[i] == "K":
            if Kksa % 3 == 0:
                Kksa += 1
            if Sksa % 3 == 2:
                Sksa += 1
            if Aksa % 3 == 1:
                Aksa += 1
        elif ksa[i] == "S":
            if Kksa % 3 == 1:
                Kksa += 1
            if Sksa % 3 == 0:
                Sksa += 1
            if Aksa % 3 == 2:
                Aksa += 1
        elif ksa[i] == "A":
            if Kksa % 3 == 2:
                Kksa += 1
            if Sksa % 3 == 1:
                Sksa += 1
            if Aksa % 3 == 0:
                Aksa += 1

    maxKSA = max(Kksa, Sksa, Aksa)

    if maxKSA == Kksa:
        print((len(ksa) - maxKSA) * 2)

    elif maxKSA == Sksa:
        if len(ksa) - maxKSA == 0: # KSAKSAKS
            print(2)
        else:
            print((len(ksa) - maxKSA) * 2)

    else:
        if len(ksa) - maxKSA == 0: # KSAKSAK
            print(2)
        elif len(ksa) - maxKSA == 1: # AKSAA
            print(4)
        else:
            print((len(ksa) - maxKSA) * 2)