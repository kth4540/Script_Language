# def add(a,b):
#     sum=a+b
#     return sum
#
# result=add(100,10)
# print(result)
#
# result=add('hello','world')
# print(result)

###############################

# print('hello',end=' ')
# print('world')
#print('cats','dogs','mice',sep=',')

################################

# def spam():
#     global eggs
#     eggs='spam'
#
# def bacon():
#     eggs='bacon'
#
# def ham():
#     print(eggs)
#
# eggs=42
# spam()
# print(eggs)
# bacon()
#ham()

#######################

# def sum_and_mul(a,b):
#     return a+b,a*b
#
# num=sum_and_mul(3,4)
# print(num)
# num,_=sum_and_mul(3,4)
# print(num)

##############################

# def add(a,b):
#     return a+b
#
# def mul(a,b):
#     return a*b
#
# myFunc=add
# print(myFunc(1,3))

#################################

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: invalid argument')

print(spam(2))
print(spam(0))