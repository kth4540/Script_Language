# from builtins import classmethod
#
#
# class FamilyMember:
#     last_name='Lee'
#
#     def __init__(self,name,age):
#         self.name,self.age=name,age
#
#     @classmethod
#     def from_age(cls,age=0):
#         return cls('NONAME',age)
#     # cls를 return -> __init__ 호출
#
#     @classmethod
#     def from_name(cls,name='NONAMAE'):
#         return cls(name,0)
#
#     @staticmethod
#     def help():
#         print(f"This is FamilyMember class with last name {FamilyMember.last_name}")
#
#     def introduce(self):
#         print(f"i'm {self.name} {FamilyMember.last_name} and {self.age} years old")
#
# father=FamilyMember('John',60)
# son=FamilyMember.from_age(10)
# mother=FamilyMember.from_name('suji')

class Figure:
    def info(self):
        print(self.name)
    pass

class Circle(Figure):
    name='CIRCLE'
    def __init__(self,radius=10):
        self.radius=radius
        print(f'with radius {self.radius}')
    pass

class Square(Figure):
    name='SQUARE'
    def __init__(self,length=10):
        self.length=10
    pass