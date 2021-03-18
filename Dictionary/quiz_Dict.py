import random
def kor_avg(a):
    sum=0
    tmp={}
    for c in range(0,20):
        tmp=a[c]
        sum+=tmp['KOR']
    return sum/20

def eng_avg(a):
    sum=0
    tmp={}
    for c in range(0,20):
        tmp=a[c]
        sum+=tmp['ENG']
    return sum/20

def math_avg(a):
    sum=0
    tmp={}
    for c in range(0,20):
        tmp=a[c]
        sum+=tmp['MATH']
    return sum/20

score={}

students=[]
for c in range(0,20):
    score['KOR']=random.randint(1, 100+1)
    score['ENG']=random.randint(1, 100+1)
    score['MATH']=random.randint(1, 100+1)

    students.append(score)

for c in range(0,20):
    print(students[c],'\n')

print(kor_avg(students),eng_avg(students),math_avg(students))