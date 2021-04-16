import shutil
import os

# shutil.copy('test.txt','copytest.txt')  #파일 복사
# shutil.copy('test.txt','./lecture')
#
# shutil.copytree('.','lecture') #폴더를 통째로 복사
#
# shutil.move('lecture','newlecture')   #폴더를 통째로 이동

#-------------------------------------------#

import zipfile

# zip=zipfile.ZipFile('test.zip')
# print(zip.namelist())
# info=zip.getinfo('ch_1_1.txt')
#
# print(info.file_size)
# print(info.compress_size)
# zip.close()
#
# zip=zipfile.ZipFile('test.zip')
#
# os.mkdir('result')
# os.chdir('result')
# zip.extractall()
# print(os.listdir())
# zip.close()

#-----------------------------#
# newZip=zipfile.ZipFile('new.zip','w')
# newZip.write('copytest.txt',compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()
#
newZip=zipfile.ZipFile('myZip.zip','w')
newZip.write('copytest.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.write('copy2.txt',compress_type=zipfile.ZIP_DEFLATED)

newZip.close()

#-----------------------------#
import datetime
print(datetime.datetime.fromtimestamp(os.path.getmtime('copytest.txt')).strftime('%Y%m%d'))