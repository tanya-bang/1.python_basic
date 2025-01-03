import re
from util import check_re

def reg_exp1():
    # 정규표현식
    # r'', re.compile()
    exp = r'python'
    text = 'easy python lib python regular expression'
    
# 자주 사용하는 메서드 사용해보기
# 1. search : 문자열 전체 탐색
    res = re.search(exp, text)
    if(res):
        print('search', res.group())
    else:
        print('not exists')
 
# 2. match: 문자열 시작부분을 탐색
    res = re.match(exp, text)
    if(res):
        print('match:', res.group())
    else:
        print('match:', 'not exist')

# 3. split
    res = re.split(exp, text)
    print(res)

# 4. findall
    res = re.findall(exp, text)
    print(res)
    
#reg_exp1()

def reg_exp2():
    """
    앵커문자
    ^ : ^ 뒤에 오는 패턴으로 시작하는 문자열 줄인가를 검증
    $ : $ 앞에 오는 패턴으로 종료되는 문자열 줄인가를 검증
    """
    
    text = 'python script is a module'
    text2 = 'is script a module in python'
    
    exp = r'^python' 
    exp2 = r'python$' 
    # 문자열이 python으로 시작하는가?
    check_re(exp, text)
    check_re(exp, text2)
    
    # 문자열이 python으로 끝나는가?
    check_re(exp2, text)
    check_re(exp2, text2)
    
#reg_exp2()


def reg_exp3():
    """
    flag 문자
    정규표현식이 탐색할 범위를 지정
    i: 대소문자를 구분하지 않고 검색
    m: 모든 행에 대해 패턴을 검색
    """
    
    text = """PYTHON, javajscript
    html, css, matplotlib python
    database, pandas"""
    
    exp = r'^python'
    exp_f = r'(?i)^python' #i flag를 적용시킨다는 뜻 
    exp2 = r'python$'
    exp2_f = r'(?m)python$'
    
    check_re(exp,text)
    check_re(exp_f, text)
    check_re(exp, text, re.IGNORECASE)
    
    check_re(exp2, text)
    check_re(exp2_f, text)
    check_re(exp2, text, re.MULTILINE | re.IGNORECASE)
    
#reg_exp3()

def reg_exp4():
    """
    문자셋
    []로 묶어준다.
    문자셋 안의 패턴은 or 연산으로 수행된다.
    [] 안에서 ^는 not의 의미를 가진다. #앵커할 떄 ^와 다르게 사용됨을 기억!
    
    1. 숫자 : [0-9]
    2. 알파벳소문자: [a-z]
    3. 알파벳대문자: [A-Z]
    4. 알파벳: [a-zA-Z]
    5. 한글: [ㄱ-힣]
        UTF파일에서만 지정되지만 파이썬은 무조건 그 파일만 사용함 어차피 ㅇㅇ
    6. 특수문자: [^a-zA-Z0-9ㄱ-힣] :이것들이 다 아니면 특문으로 보는 것.
    """
    # escape문자
    # \'
    # \"
    # \n, \r\n : 줄바꿈
    # \t : tab
    # \b : backspace
        
    text = """1. PYTHON, 2.javajscript
    3.html, 4.css, 5.matplotlib 6.파이썬
    7.database, 8.판다스"""
    
    exp_num = r'[0-9]' # r'[0123456789]
    exp_lower_case = r'[a-z]'
    exp_upper_case = r'[A-Z]'
    exp_alpha = r'[a-zA-Z]'
    exp_kor = r'[ㄱ-힣]'
    exp_etc = r'[^a-zA-Z0-9ㄱ-힣\n]'
    print(re.sub(exp_num, '*', text))
    print('----------------------------')
    print(re.sub(exp_lower_case, '*', text))
    print('----------------------------')
    print(re.sub(exp_upper_case, '*', text))
    print('----------------------------')
    print(re.sub(exp_alpha, '*', text))
    print('----------------------------')
    print(re.sub(exp_kor, '*', text))
    print('----------------------------')
    print(re.sub(exp_etc, '*', text))
    # 줄바꿈도 깨짐..! 줄바꿈 깨지는게 싫으면 힣뒤에 \n 붙이면 됨.
    
#reg_exp4()
    """exp_kor = r'[ㄱ-힣]' 하면 한글 한글자짜리 변경
       exp_kor = r'[ㄱ-힣][ㄱ-힣]' 하면 한글 두글자 변경
       exp_kor = r'[ㄱ-힣][ㄱ-힣][ㄱ-힣]'하면 세글자!
    """

def reg_national_id():
    """
    주민등록번호를 검증하는 정규표현식을 만드시오
    숫자 6자리 - 숫자 7자리
    주민등록번호의 - 뒤 첫 숫자는 1-4 사이의 숫자만 올 수 있다.
    """
    exp = r'[0-9][0-9][0-9][0-9][0-9][0-9]-[1-4][0-9][0-9][0-9][0-9][0-9][0-9]'
    text = 'name,19,lec,000000-1000000,서울시,강남구'
    check_re(exp, text)
    
#reg_national_id()

def reg_exp5():
    # 특수문자
    # . : 줄바꿈문자를 제외한 모든 단일 문자
    # \d : 숫자 =[0-9]
    # \D : 숫자가 아닌 =[^0-9]
    # \w : 밑줄 문자를 포함한 영수문자 =[a-zA-Z0-9_]
    # \W : 밑줄 문자를 포함한 영수문자가 아닌 =[^a-zA-Z0-9_]
    # 이렇게 줄여서 표현하자고 약속함
    # cf) 파이썬에서는 \w, \W에서 영수문자+한글까지 변환해줌
    
    # 수량문자 (BNF표기법에서 본 적이 있대. 물론 나는 기억이 없지 ^^)
    # + : 패턴이 1개 이상 존재
    # * : 패턴이 0개 이상 존재
    # ? : 패턴이 0개 또는 1개 존재
    # {n} : 패턴이 n개 존재
    # {n,m} : 패턴이 0~m개 존재
    # {n,} : 패턴이 n개 이상 존재

    text = text = """1. PYTHON, 2.java___script
    3.html, 4.css, 5.matplotlib 6.파이썬
    7.database, 8.판다스 
    """
    print('줄바꿈빼고 .:', re.sub(r'.','*', text))
    print('----------------------')
    print('숫자: ', re.sub(r'\d','*', text))
    print('----------------------')
    print('숫자빼고:', re.sub(r'\D','*', text))
    print('----------------------')
    print('w: ', re.sub(r'\w','*', text))
    print('----------------------')
    print('W: ', re.sub(r'\W','*', text))
    print('----------------------')
    
    exp = r'\d{6}-[1-4]/d{6}'
    text = 'name,19,lec,000000-1000000,서울시,강남구'
    check_re(exp, text)
    
#reg_exp5()

def reg_exp6():
    """
    () : 그룹
    | : 그룹 안에서 |를 사용해 패턴을 or로 묶어줄 수 있다.
    
    주민번호 최종
    연도 : 숫자 2자리    ==>   
    월 : 01-09 | 11-12  ==>    
    일 : 01-31          ==>    
    """
    exp = r'\d{2}0[1-9]|1[0-2]0[1-9]|[1-2]\d|3[0-1]-[1-4]\d{6}'
    text = 'name,19,lec,000000-1000000,서울시,강남구'
    check_re(exp, text)
    
reg_exp6()