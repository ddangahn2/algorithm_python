# S5

subjects = [input().split() for _ in range(20)]

GRADE = {'A+':4.5,'A0':4,'B+':3.5,'B0':3,'C+':2.5,'C0':2,'D+':1.5,'D0':1,'F':0}
total_credit = 0
total_grade = 0

for subject, credit, grade  in subjects:
    credit = float(credit)
    if grade != 'P':
        total_credit += credit
        total_grade += GRADE[grade] * credit

print(total_grade / total_credit)