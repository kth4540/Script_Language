import copy
import random
# black_pink=['jisu','jenny','rose','lisa']
# print(black_pink[3])
#print(black_pink[-1])

##################

# num='0123456789'
# print(num[0:5:2])
# print(type(num))
# print(num[:])
# print(num[-4:])
# print(num[::-1])
# spam=['cat','bat','rat','elephant']
# print(spam[:])
# print(spam[-4:])
# print(spam[::-1])

# spam=[['cat','rat'],[10,20,30,40,50]]
# print(spam[0])
# print(spam[1])
# print(spam[0][0])
# print(spam[1][2])

###################

# black_pink=['jisu','jenny','rose','lisa']
# black_pink[0]='hooing'
# black_pink.append('hellotron')
# black_pink=black_pink+['pepsi']
# print(black_pink)
#
# twice=['momo','sana','dahyun','nayun']
# unite=black_pink+twice
# print(unite)
# unite.remove('hooing')
# del unite[0]
# unite.insert(2,'cooky')
# print(unite)

# for member in black_pink:
#     print(member)
#
# for i in range(len(black_pink)):
#     print(i,'th member is',black_pink[i])

# for i, member in enumerate(black_pink):
#     ##enumerate 는 list memeber의 인덱스와 멤버를 받을 수 있음
#     print('%d th member is %s'%(i,black_pink[i]))

# print('daehyun' in unite)
# print('sana' in unite)
# print('daehyun' not in unite)

# cat=['fat','black','loud']
# size,color,position=cat
# print(size,color,position)
# print(cat.index('black'))

# spam=[3,-7,1.5,10]
# spam.sort()
# print(spam)
#
# black_pink.sort()
# print(black_pink)
#
# black_pink.sort(reverse=True)
# print(black_pink)

##################################

# spam=['a','b','c'',d']
# cheese=spam
# #spam의 reference가 cheeses에 복사됨
# #cheese와 spam은 동일
#
# cheese[1]=77
# print(spam)
# #cheess의 값을 바꿨지만 spam의 값이 바뀜
#
# cheese=copy.copy(spam)
# print(cheese)
# cheese[1]='hou'
# print(spam)
# print(cheese)

# a=[1,2,3]
# b=[1,2,3]
# print(a==b)     #a와 b의 멤버 값이 같은가
# print(a is b)   #a와 b가 같은가
#
# x=[1,2,3]
# y=x
# print(x==y)
# print(x is y)

####################################

# values=[i for i in range(10)]
# print(values)
#
# random_value=[random.randint(1,100)for i in range(100)]
# print(random_value)
#
# odd_value=[n for n in range(100) if n%2==1]
# print(odd_value)
#
# l=[(x,y) for x in [1,2,3] for y in ['a','b','c']]
# print(l)
#
# vec=[[1,2,3],[4,5,6],[7,8,9]]
# flat= [n for elm in vec for n in elm]
# print(flat)

##################

# value=[random.randint(0,5) for i in range(20)]
# print(value)
# new_value=[v if v!=0 else 'zero' for v in value]
# print(new_value)


