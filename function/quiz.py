import random

answer=random.randint(1,30)
str(answer)
print(answer)
num=''
while answer!=num:

    num = str(input())

    if(num=='quit'):
        print('quit')
        quit(0)


    if int(num)>int(answer):
        print('big')
    elif int(num)<int(answer):
        print('small')
    elif int(num)==int(answer):
        print('end')
        quit(0)

