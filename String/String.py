
# spam="that is alice's cat"
# spam='say hi to bob\'s mother.'
#
# print(r'HELLO')
# print(r'that is carol\'s cat')
#
# def print_line():
#     print('''
# 애국가 동해물과 백두산이~~~~
# 우리나라만세~~~
# 끝
#     ''')    #-> ''' '''그대로 출력됨
# print_line()

# print('hello' in 'hello world')
# print('Hello' in 'hello world')
# print(''in 'spam')
# print('cats'not in 'cats and dogs')

# test='hello'
# print(test.isalpha())
# print('hello123'.isalnum())
# print('123'.isdecimal())
# print('This Is Title Case'.istitle())#-> 모든 단어가 첫글자 대문자, 나머지 소문자일때
# print('hello'.upper())
#
# spam='hello'
# print(spam)
# spam.upper() #-> spam은 그대로고, 대문자로 만든 문자열을 새로 만들어서 출력
# spam=spam.upper()
# print(spam)
#
# print('hello'.isupper())
# print('hello'.islower())
# print('abc1234'.islower())

# print('hello world'.startswith('hello'))
# spam='hello world'
# spam.endswith('world')

# l=['cats','rats','bats']
# # ','.join(l)#리스트 인덱스를 연결할 문자를 먼저 지정
#print(l)

# src='''hello, my name is hooing'''
# print(src.split())
# test='my string is hooing'
# print(test.split('i'))  ##-> i을 기준으로 string
#
# test='hello'
# print(test.rjust(10))
# print(test.ljust(10))
# print(test.ljust(20,'*'))
# print(test.center(20,'*'))

# def printPicnic(itemsDict,leftWidth,rightWidth):
#     print('PICNIC ITMES'.center(leftWidth+rightWidth,'-'))
#     for k,v in itemsDict.items():
#         print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
#
# picnicItems={'sandwiches':4,'apples':12,'cups':4,'cookies':8000}
# printPicnic(picnicItems,12,5)
# printPicnic(picnicItems,20,6)

# spam=' hello, world '
# print(spam.strip()) #-> strip은 특문이나 공백같은 문자 제거
# print(spam.lstrip())
# print(spam.rstrip())
#
# spam='spamspambaconspameggsspamspam'
# print(spam.strip('amps'))  #끝만 제거되고 가운데는 살아남음

