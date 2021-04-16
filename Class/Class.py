# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def introduce(self):
#         print(f'My name is {self.name},and i\'m {self.age} years old')


# a_person=Person('taehyeok',24)
# a_person.introduce()

#-------------------------------------#

# class FamilyMember:
#     pass
# father=FamilyMember()
# isinstance(father,FamilyMember)
# father=FamilyMember()
#
# father.name='Tom'
# father.age=30
# father.address='Seoul'
#
# son=FamilyMember()
# son.name='Tom'
# son.age=10
# son.school='KPU'
#
# FamilyMember.last_name='Lee'
#
# son.last_name='Park'

#------------------------------------#

# class FamilyMember:
#     last_name='Lee'
#
#     def __init__(this, name='noname', age=8):
#         this.name, this.age= name, age
#
#     def introduce(this):
#         print(f"i'm {this.name}{FamilyMember.last_name}")
#
#     @classmethod
#     def change_last_name(cls, new_last_name):
#         cls.last_name = new_last_name
#
# father=FamilyMember('Tom',60)
# father.last_name='Kim'
# del father.last_name
#
# #FamilyMember.introduce() -> error
# FamilyMember.introduce(father)
# father.introduce()
#
# def identify(self):
#     if self.age>=18:
#         print("i'm adult")
#     else:
#         print("i'm child")
#
# def introduce_in_korean(self):
#     print(f"저는 {FamilyMember.last_name} {self.name} 입니다")

#-----------------------------------#

class FamilyMember:
    last_name='Lee'

    def __init__(self,name,age):
        self.name,self.age=name,age

    def __init(self,name):
        self.name,self.age=name,0

    def __int__(self,age):
        self.name,self.age='noname',age

