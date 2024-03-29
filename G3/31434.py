# G3
# [2024 KSA Automata Winter Contest · Arena #22](https://www.acmicpc.net/contest/view/1238)


import sys
input = sys.stdin.readline

# N개 버튼, K초 실행

N, K = map(int, input().split())

carrot_btn_dict = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a not in carrot_btn_dict:
        carrot_btn_dict[a] = b
    else:
        carrot_btn_dict[a] = max(b, carrot_btn_dict[a])

# 쓸모없는 버튼들 제거
carrot_btn = list(carrot_btn_dict.items())

pre_state = [(0, 1)]
cur_state = []

def get_carrot():
    temp_state = {}
    for carrot, produce in pre_state:
        if produce not in temp_state:
            temp_state[produce] = carrot + produce
        else:
            temp_state[produce] = max(temp_state[produce], carrot + produce)
    
    return [(x, y) for y, x in temp_state.items()]

def get_speed():
    temp_state = {}
    for carrot, produce in pre_state:
        for minus_carrot, plus_produce in carrot_btn:
            if produce not in temp_state:
                temp_state[produce] = carrot + produce
            else:
                temp_state[produce] = max(temp_state[produce], carrot + produce)
            
            if carrot >= minus_carrot:
                if (produce + plus_produce) not in temp_state:
                    temp_state[produce + plus_produce] = carrot - minus_carrot
                else:
                    temp_state[produce + plus_produce] = max(temp_state[produce + plus_produce], carrot - minus_carrot)
    
    return [(x, y) for y, x in temp_state.items()]

# 1초와 마지막초는 무조건 버튼을 눌러야함
for time in range(K):
    if time == 0 or time == K-1:
        cur_state = get_carrot()
    else:
        cur_state = get_speed()
    
    if time == K-1:
        print(max([carrot for carrot, produce in cur_state]))
    else:
        pre_state = cur_state