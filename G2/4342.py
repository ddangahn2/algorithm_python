# G2 solved

# 0이면 혁 win, 1이면 규 win
while True:
    A, B = map(int, input().split())
    
    if A == 0 and B == 0:
        break

    winner = 0
    turn = -1
    turn_count = 0

    while A != 0 and B != 0:
        if A < B:
            A, B = B, A

        if A % B == 0:
            break

        if A > 2*B and turn_count == 0:
            turn = winner
            turn_count = 1
            break
        A %= B
        winner = 1 - winner

    if turn == 1:
        print("B wins")
    elif turn == 0:
        print("A wins")
    else:
        if winner == 0:
            print("A wins")
        elif winner == 1:
            print("B wins")