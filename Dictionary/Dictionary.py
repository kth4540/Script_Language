from _operator import and_

# a_student={}
# print(type(a_student))
# a_student={'name':'kim','grade':'A+'}
# print(a_student['name'])
# a_student['age']=24
# print(a_student)
#
# b_student={'name': 'kim', 'grade': 'A+', 'age': 24}
# print(a_student==b_student)
#
# c_student={ 'grade': 'A+', 'age': 24,'name': 'kim'}
# print(a_student==c_student)
# #dictionary는 순서 상관 없음
#
# for key in a_student.keys():
#     print(key)
# for value in a_student.values():
#     print(value)
# for item in a_student.items():
#     print(item)
# # key 와 value를 tuple로 저장하고 있음
#
# print('name' in a_student.keys())
# print('kim' in a_student.values())
#
# a_student.get('name',176)
# # key가 없을 경우 default 값 설정 가능

# text='It was a bright cold day in april, and the clocks were striking thirteen.'
# count={}
# for c in text:
#     count.setdefault(c,0) -> 받아들인 문자의 초기 value 설정
#     count[c]=count[c]+1   -> 이후 value 증가
#print(count)

s1={1,2,2,2,3}
print(s1)
s2={2,1,3}
print(s1==s2)

s2={1,2,4,5}
print(s1|s2)
print(s1&s2)
print(s2-s1)
s1.add(5)
s1.remove(2)
print(s1)