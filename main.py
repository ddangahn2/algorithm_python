# 문제 난이도 어땠는지 (형식: B2)
# 몇번 풀었는지
# 추가 관련사항 있는지

import re
import shutil

def add_last_line_to_readme(line_to_add):
    with open("README.md", "a") as readme:
        readme.write("\n" + line_to_add)

def read_last_line():
    with open("README.md", "r") as readme:
        lines = readme.readlines()
        if lines:
            return lines[-1].strip()

def add_first_line_to_readme(line_to_add):
    with open("README.md", "r") as readme:
        lines = readme.readlines()
    
    start_index = 0

    for index, line in enumerate(lines, start=1):
        if line.startswith("|1|"):
            start_index = index
            break

    lines.insert(start_index - 1, line_to_add + '\n')
    
    # start_index부터 숫자 추가
    start_index_temp = start_index

    for line in lines[start_index:]:
        line_index = parse_line_index(line)
        if line_index == None:
            break
        else:
            new_line_index = int(line_index) + 1
            lines[start_index_temp] = line.replace(f"|{line_index}|",f"|{new_line_index}|")
            start_index_temp += 1

    with open("README.md", 'w') as file:
            file.writelines(lines)

def parse_line_index(line):
    match = re.search(r'\|(\S+?)\|', line)
    if match:
        return match.group(1)
    else:
        return None

print("문제 난이도를 입력하세요(형식 B2, G1): ", end='')
difficulty = input()

print("몇번 문제를 풀었나요?: ", end='')
problem_index = int(input())

print("추가 기록사항이 있나요?: ", end='')
description = input()

print("오늘이 몇년인가요?: ", end='')
added_year = input()

print("오늘이 몇월인가요?: ", end='')
added_month = input()

print("오늘이 몇일인가요?: ", end='')
added_day = input()

print("런타임에러나 타임아웃등 에러명을 적어주세요: ", end='')
other_problem = input()

line_to_add = f"|1|[{difficulty}](https://github.com/sangahnhan/algorithm_python/tree/main/{difficulty})|[{problem_index}](https://www.acmicpc.net/problem/{problem_index})|[풀이](https://github.com/sangahnhan/algorithm_python/blob/main/{difficulty}/{problem_index}.py)|{description}|{added_year}/{added_month}/{added_day}|{other_problem}|"
# add_last_line_to_readme(line_to_add)

# add_first_line_to_readme(line_to_add)

# python 파일 난이도 파일로 옮기기
# 파일 이름은 문제번호로 ex. 11044.py -> B2/11044.py
problem_file_name = f"{problem_index}.py"

shutil.move(problem_file_name, f"{difficulty}/{problem_file_name}")
