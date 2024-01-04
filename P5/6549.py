# P5 solved

while True:
    line = list(map(int, input().split()))

    if line[0] == 0:
        break

    n = line[0]

    max_area = 0
    height_list = []

    for i in range(1,n+1):
        if height_list == []:
            height_list.append([i,line[i]])
        else:
            # 현재 height와 비교
            if height_list[-1][1] < line[i]:
                height_list.append([i,line[i]])
            else:
                min_index = n+1

                while height_list != [] and height_list[-1][1] > line[i]:
                    max_area = max(max_area, (i - height_list[-1][0]) * height_list[-1][1])
                    min_index = min(min_index, height_list[-1][0])
                    height_list.pop()
                height_list.append([min_index,line[i]])

    while height_list != []:
        max_area = max(max_area, (n + 1 - height_list[-1][0]) * height_list[-1][1])
        height_list.pop()

    print(max_area)