# t1=(1,2,3)
# print(type(t1))
# #t1[0]=1    -> tuple의 값은 변경 불가능
#
# def sum(*values):
#     result=0
#     for v in values:
#         result+=v
#     return result
#
# print(sum(1,2,3))
#print(sum(2,4,6))

###################

l=['cat','dog',5]
print(type(l))
t=tuple(l)
print(type(t))

a=list('hello')
print(a)