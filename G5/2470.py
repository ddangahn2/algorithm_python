# G5 solved

N = int(input())

n_list = sorted(list(map(int, input().split())))

start = 0
end = N-1

temp_s = start
temp_e = end

total_min = n_list[start] + n_list[end]

while start < end:
    local_min = n_list[start] + n_list[end]

    if abs(total_min) > abs(local_min):
        total_min = local_min
        temp_s = start
        temp_e = end
    else:
        if local_min <= 0:
            start += 1
        else:
            end -= 1

print(n_list[temp_s], n_list[temp_e])
