import re

# hello_re=re.compile(r'hello')
# print(hello_re.search('hello world'))
# print(hello_re.search('test'))

#--------------------------------------------#

# phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo=phoneNumRegex.search('my number is 415-555-4242')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group())
# print(mo.groups())
# areaCode,mainNumber=mo.groups()
# print(areaCode)
# print(mainNumber)

#----------------------------------------------#

# ne=re.compile(r'(jisu|rose)')
# print(ne.search('blackpink members are jisu and rose'))
# print(ne.search('blackpink members are rose and jisu'))

#-----------------------------------------------#

# ne=re.compile(r'Bat(wo)?man')
# print(ne.search('Batman'))
# print(ne.search('Batwoman'))

#------------------------------------------------#

# greedyHaRegex=re.compile(r'(Ha){3,5}')  #-> default는 최대를 찾음(Greedy)
# mo1=greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())
#
# nongreedyHaRegex=re.compile(r'(Ha){3,5}?')  #-> 먼저 발견된 것을 찾음(Non-Greedy)
# mo2=nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo2.group())

#-------------------------------------------------#

# phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneNumRegex.findall('home=031-123-4567, office=031-987-6543'))

#-------------------------------------------------#

all_re=re.compile(r'first:(.*) last:(.*)')
mo=all_re.search('first:taehyeok last:kim ')
print(mo)

##줄바꿈 무시=re.dotall
##대소문자 무시=re.I

#--------------------------------------------------#

namesRegex=re.compile(r'Agent \w+')
namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')

agentNamesRegex=re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
