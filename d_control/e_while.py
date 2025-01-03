"""
반복문

while(조건식):
    조건식이 참일 때 반복실행할 코드블록
"""

#while(1 == 1):
#   print('비상!!!') 이렇게 해서 실행하면 조건식이 언제나 참이니까 무한반복됨;;;

def study_while_count():
    """'안녕 파이썬'을 다섯번 출력하는 while문을 작성하세요.
    meaning that 코드블록이 5번 반복되었을 때 while의 조건식을 False로 만들어준다.
    """
    i = 0
    # i : 0, 1, 2, 3, 4, 5
    while(i < 5):
        print('안녕 파이썬')
        i += 1 #반드시 i는 1씩 증가해야해!
    print('반복문 종료')
study_while_count()

def study_while():
    """사용자로부터 아이디와 비밀번호를 입력받아
        인증정보가 일치하면 로그인 처리,
        일치하지 않으면 다시 입력받도록 하는 프로그램을 구현하시오

        id: python
        password: 1111

        일치할 경우 메세지 : 로그인 되었습니다.
        일치하지 않을 경우 : 로그인에 실패했습니다.
    """

    stored_id = 'python'
    stored_password = '1111'

    user = 'anonymous'
    while(user == 'anonymous'):
        id = input('id: ')
        password = input('password: ')

        if(stored_id == id and stored_password == password):
            user = id
            print('로그인 되었습니다.')
        else:
            print('로그인에 실패했습니다.')
        
        try_cnt += 1
        if(try_cnt >= 5):
            print('로그인 시도 횟수를 초과했습니다')
            user = 'blocked'
    else:
        print('환영한다.')

def q6() :
    """
    가위바위보를 하는 프로그램을 구현해주세요.
    사용자로부터 userA와 userB의 패를 입력받으세요.
    패 : 가위 | 바위 | 보
    3판 2선승 제도를 따를 것이며
    userA기준에서 승무패를 출력해주시면 됩니다.
    """
    


        
    

    