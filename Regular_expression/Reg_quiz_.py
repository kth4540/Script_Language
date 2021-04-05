import re

def check_num(num):
    check_dialing=re.compile('''
    ^
    \d{3,4}
    (\s|-)?
    \d{4}
    $
    ''',re.VERBOSE) #지역번호가 존재하는지 확인

    check_area=re.compile('''
    ^
    (
(02|010|03[1|2|3]|04[1|2|3|4]|05[1|2|3|4|5]|06[1|2|3|4])    # 지역번호 ()없이
|
\((02|010|03[1|2|3]|04[1|2|3|4]|05[1|2|3|4|5]|06[1|2|3|4])\)# 지역번호 ()포함
)
    ''',re.VERBOSE) # 지역번호가 유효한지 확인

    phone_re = re.compile('''
^
(
(02|010|03[1|2|3]|04[1|2|3|4]|05[1|2|3|4|5]|06[1|2|3|4])    # 지역번호 ()없이
|
\((02|010|03[1|2|3]|04[1|2|3|4]|05[1|2|3|4|5]|06[1|2|3|4])\)# 지역번호 ()포함
)
(\s|-)?                                                     # '-' 또는 공백 여부
\d{3,4}                                                     # 3자리 또는 4자리
(\s|-)?                                                     # '-' 또는 공백 여부
\d{4}                                                       # 4자리
$
''', re.VERBOSE)
    if check_dialing.search(num):
        num='010-'+num                   #지역번호가 없으면 번호에 010 추가

    if not check_area.search(num):
        print('wrong local number')     #지역번호가 유효하지 않으면 에러 메시지 출력
        return

    print(phone_re.search(num))         #이상 없으면 번호 출력

test_num=['(031)-555-6666','5556666','666-777-8888','010-33-444']   #테스트셋

for i in test_num:
    check_num(i)