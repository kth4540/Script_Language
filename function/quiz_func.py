import random

answer=random.randint(1,30)
while(True):
    number=input()

    if number=='quit':
        print('quit')
        break

    try:
        number=int(number)

    except ValueError:
        print('wrong input')
        continue

    if int(number)>answer:
        print('bigger')
        continue

    elif int(number)<answer:
        print('smaller')
        continue
    else:
        print('correct')
        break
