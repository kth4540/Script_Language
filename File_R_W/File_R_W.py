import os
import shelve
import random

# print(os.getcwd())
# #os.chdir('c:/windows/system32')
# print(os.getcwd())              #-> 현재 디렉토리
# print(os.path.abspath('.'))     #-> 절대경로 출력
# print(os.listdir())             #-디렉토리의 파일들 출력
# #os.mkdir('sub')
# print(os.path.abspath('sub'))

#------------------------------------#

# abs_path=os.path.abspath('list.py')
# os.path.basename(abs_path)
# os.path.dirname(abs_path)

#-------------------------------------#

# os.chdir('c:/windows/system32')
# print(os.path.getsize('calc.exe'))
#
# total_size=0
# for fn in os.listdir():
#     total_size+=os.path.getsize(fn)
# print(total_size)

#-------------------------------------#

# for root,subfolders, filenames in os.walk('.'):
#     print(('ROOT: '+root+' ').center(80,'='))
#     print('Subfolder: '.ljust(15),subfolders)
#     print('files: '.ljust(15),filenames)
#     print('\n')

#---------------------------------------#
from setuptools.command.egg_info import write_file

# f=open('READ_ONLY.py')
# print(f.read())
# print(f.read())
# f.seek(0)
# print(f.readline())
# f.seek(0)
# print(f.readlines())
# f.close()
#
# w_file=open('mydata.txt','w')
# w_file.write('hello this is my data\n')
# w_file.close()
#
# w_file=open('mydata.txt','a')
# w_file.write('new hello\n')
# w_file.close()

#--------------------------------------#


# data=[random.randint(0,100) for i in range(100)]
# print(data)
#
# #파일 쓰기
# data_file=shelve.open('data')
# data_file['data']=data
# data_file.close()
#
# #파일 읽기
# read_file=shelve.open('data')
# new_data=read_file['data']
# read_file.close()
#
# print(new_data)

#----------------------------------------------#

def get_key(x):
    return x[0]

data={'jisu':100,'momo':20,'rose':200,'iu':3}
result=sorted(data.items(),key=get_key,reverse=True)
print(result)

