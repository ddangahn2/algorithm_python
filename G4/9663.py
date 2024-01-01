# G4 solved

N = int(input())

# 퀸은 한줄에 하나씩 들어가야한다
# 퀸의 왼쪽 아래 대각선은 합이 같다
# 퀸의 오른쪽 아래 대각선은 차가 같다
# 퀸의 아래 대각선은 x좌표가 같다

count = 0
queen_x_pos_list = []

def possible_move(pos_list, queen_x_pos):
    queen_y_pos = len(pos_list)

    for index, pos in enumerate(pos_list):
        if pos == queen_x_pos or (queen_y_pos + queen_x_pos) == index + pos or (queen_y_pos - queen_x_pos) == (index - pos):
            return False
    return True

def n_queen(queen_y_pos):
    global count

    if queen_y_pos == N:
        count += 1
        return
    
    for queen_x_pos in range(N):
        if queen_x_pos_list == []:
            queen_x_pos_list.append(queen_x_pos)
            n_queen(queen_y_pos + 1)
            queen_x_pos_list.pop()
        elif possible_move(queen_x_pos_list, queen_x_pos):
            queen_x_pos_list.append(queen_x_pos)
            n_queen(queen_y_pos + 1)
            queen_x_pos_list.pop()
        
n_queen(0)

print(count)