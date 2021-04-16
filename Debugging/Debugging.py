# while True:
#     try:
#         age=int(input('enter age: '))
#         if age<18:
#             raise Exception('too young')
#     except Exception as err:
#         print('ERROR: ',err)

#-------------------------------------------#

# import traceback
# def bacon():
#     try:
#         raise Exception('My error')
#     except:
#         ef=open('error_log.txt','w')
#         for l in traceback.format_stack():
#             ef.write(l)
#         ef.close()
#
# def spam():
#     bacon()
#
# spam()

#----------------------------------------#

# age=int(input('enter age: '))
# # age는 정수라는 확신이 필요
# assert type(age) is int,"age should be integer"
# if age<18:
#     print('too young')
#
# #-----------------------------------------#
#
# while True:
#     try:
#         age=int(input('enter age: '))
#         if age<18:
#             raise Exception('too young')
#     except Exception as err:
#         #write error to file
#         pass

#------------------------------------------#
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

logging.warning('warning')
logging.debug('DEBUG LOG')