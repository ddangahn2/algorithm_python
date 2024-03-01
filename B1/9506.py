# B1 solved

while True:
    a = int(input())
    if a == -1:
        break
    else:
        div = set()
        root_a = int(a ** 0.5)
        div.add(1)
        for i in range(2, root_a+1):
            if a % i == 0:
                div.add(i)
                div.add(a//i)
        
        list_div = list(div)
        if sum(list_div) == a:
            list_div.sort()
            print(f"{a} = {list_div[0]}",end='')
            for i in range(1, len(list_div)):
                print(f" + {list_div[i]}", end='')
            print()
        else:
            print(f"{a} is NOT perfect.")