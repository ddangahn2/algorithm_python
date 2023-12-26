N = int(input())

students = map(int,input().split())
    
B, C = map(int,input().split())

sum = 0

for i in students:
    if i <= B:
        sum += 1
    else:
        i -= B
        if i % C == 0:
            sum += (i//C + 1)
        else:
            sum += (i//C + 2)

print(sum)