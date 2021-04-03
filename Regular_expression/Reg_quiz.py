import re

numberRegex=re.compile(r'''((\d\d)(\d)*)* #AREA CODE
(-)?( )? #SEPARATOR
(\d\d\d)(\d)? # 3 OR 4 DIGITS
(-)?( )? #SEPARATOR
(\d\d\d\d) # 4 DIGITS
''',re.VERBOSE)

phoneNum=numberRegex.search('010-2622-4540')

if phoneNum==None:
    print('wrong number')
else:
    print(phoneNum.group())