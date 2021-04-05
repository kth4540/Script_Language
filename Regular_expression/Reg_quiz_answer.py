import re

phone_re = re.compile('''
02|\d{3}    # 02 031과 매칭
''', re.VERBOSE)

phone_re = re.compile('''
\(02\)|\(\d{3}\)   # 02 031과 매칭
''', re.VERBOSE)

phone_re = re.compile('''
02|\d{3}    # 02 031과 매칭
|
\(02\)|\(\d{3}\)   # (02) (031)과 매칭
''', re.VERBOSE)

phone_re = re.compile('''
^
(
(02|\d{3})    # 02 031과 매칭
|
\(
(02|\d{3})    # (02) (031)과 매칭
\)
)
$
''', re.VERBOSE)

good_str = ['02', '031','(02','(031)']
bad_str=['33','3523','[1234]','(010']
#       02 333 (02) (031) ->\(\d{3}\)

def good_test(l):
    for i in l:
        print(phone_re.search(i))
def report_test(l):
    for i in l:
        mo=phone_re.search(i)
        if mo:
            print('succes for '+i)
            print(' matching object: ',mo)
        else:
            print('fail for '+i)

report_test(bad_str)

#----------------------맨 앞 3자리------------------#

phone_re=re.compile('''
^
(
\d{3,4} # 3 OR 4 DIGITS

(\s|-) #SEPARATOR

\d{4} # 4 DIGITS
)
$
''',re.VERBOSE)

middle_str=['123-3456','333 4444','5555-6666']

def report_test_2(l):
    for i in l:
        print(phone_re.search(i))

report_test_2(middle_str)