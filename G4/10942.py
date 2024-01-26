# G4 solved

import sys
input = sys.stdin.readline

N = int(input())

board = list(map(int, input().split()))

M = int(input())

# 중간수와 떨어진 거리 저장해서 사용
pelindrom_mid = {}

# check란 끝에서부터 몇번 체크할건지
def pelindrom(S, E):
    S -= 1
    E -= 1

    if (S + E) % 2 == 0:
        left, right = (S + E) // 2, (S + E) // 2
    else:
        left, right = (S + E - 1) // 2, (S + E + 1) // 2
    # (0,3) => (1,2)
    mid = (left, right)
    already_know_pelindrom_len = -1

    if mid in pelindrom_mid:
        already_know_pelindrom_len = pelindrom_mid[mid]
    else:
        pelindrom_mid[mid] = already_know_pelindrom_len
    # 1 5 => 3 3
    # 1 6 => 3 4
    if (left - S) <= already_know_pelindrom_len:
        return True
    left -= (already_know_pelindrom_len + 1)
    right += (already_know_pelindrom_len + 1)

    while S <= left:
        if board[left] != board[right]:
            return False
        pelindrom_mid[mid] += 1
        right += 1
        left -= 1
    return True

for i in range(M):
    S, E = map(int, input().split())
    if pelindrom(S, E):
        print(1)
    else:
        print(0)
