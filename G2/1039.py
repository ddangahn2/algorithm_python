# G2 solved

N, K = map(int, input().split())

# 자리수 구하기
M = 0
power_10 = 1
while power_10 <= N:
    power_10 *= 10
    M += 1

flag = 0
# 2자리수인데 10의 배수이면 연산 불가능 / 1자리수일때 연산 불가능 -> 그 외에 모두 가능
if M == 1 or (M == 2 and N % 10 == 0):
    flag = 1
    print(-1)

# 자리수-1 만큼 교환하면 최대수 나오니까 2씩 반복이 생긴다.
while K > (M-1):
    K -= 2

NList = list(map(int, str(N)))

num_count = {}
same_number = 0
for i in NList:
    if i not in num_count:
        num_count[i] = 1
    else:
        num_count[i] += 1
        same_number = 1

sorted_index = 0
changed = K

big_num = 0
def change(num, sorted_index, change_left):
    global big_num
    if change_left == 0:
        local_num = int(''.join(str(x) for x in num))
        big_num = max(big_num, local_num)
    else:
        # 다 sorted된 상황
        if sorted_index == M-1:
            if same_number == 1 and NList[sorted_index-1] > NList[sorted_index]:
                change(num, sorted_index, change_left - 1)
            else:
                num[sorted_index-1], num[sorted_index] = num[sorted_index], num[sorted_index-1]
                change(num, sorted_index, change_left - 1)
        else:
            # sorting 하는 상황
            select = num[sorted_index]
            local_max = select
            local_max_index = sorted_index
            for j in range(sorted_index+1, M):
                if num[j] > local_max:
                    local_max = num[j]
                    local_max_index = j
            # 이미 sorted된 index
            if select == local_max:
                sorted_index += 1
                change(num, sorted_index, change_left)
            # 뒤에 바꿀 숫자가 1개인 경우
            elif num_count[local_max] == 1:
                num[sorted_index], num[local_max_index] = num[local_max_index], num[sorted_index]
                sorted_index += 1
                change(num, sorted_index, change_left - 1)
            # 뒤에 바꿀 숫자가 여러개인 경우
            else:
                max_indices = [j for j, x in enumerate(num[sorted_index+1:], start=sorted_index+1) if x == local_max]
                temp_sorted_index = sorted_index
                for max_index in max_indices:
                    num[temp_sorted_index], num[max_index] = num[max_index], num[temp_sorted_index]
                    change(num[:], sorted_index + 1, change_left - 1)
                    num[temp_sorted_index], num[max_index] = num[max_index], num[temp_sorted_index]  # 원상복구

if not flag:
    change(NList, 0, changed)
    print(big_num)