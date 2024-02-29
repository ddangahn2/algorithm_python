# G5 solved

from itertools import combinations

L, C = map(int, input().split())

word = input().strip().split()
word.sort()

vowel = ['a','e','i','o','u']
res = []

def can_pw(pw):
    vowel_flag = False
    consonant_flag = 0
    for i in pw:
        if i in vowel:
            vowel_flag = True
        elif consonant_flag < 2:
            consonant_flag += 1
    if vowel_flag and consonant_flag == 2:
        return True
    return False

password = list(combinations(word, L))

for pw in password:
    if can_pw(pw):
        print("".join(pw))