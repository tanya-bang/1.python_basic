def q1(hasegg):
    """ 매개변수로 계란의 유무를 입력받고
    개발자가 사올 우유의 개수를 출력해주는 코드를 작성하세요.
    아내: 우유 1개 사와. 아, 계란 있으면 6개 사오고.
    """
    milkcnt = 1
    if (hasegg):
        milkcnt = 6
    print(f'우유{milkcnt}개 사왔어!')

#q1(True)
#q1(False)


def q2_review(number):
    """ 매개변수로 전달된 숫자가 양수인지 음수인지 0인지 판단하는 코드를 작성하시오.
    """
    if(number > 0):
        print('양수입니다.')
    else:
        if(number <0):
            print('음수입니다.')
        else:
            print('0입니다')
#q2_review(-1)
#q2_review(3)
#q2_review(0)


def q3_review(score):
    """
    매개변수로 점수를 전달 받아 등급을 출력하세요.
    90점 이상이면 A
	80점 이상 90점 미만이면 B
	70점 이상 80점 미만이면 C
	60점 이상 70점 미만이면 D
	60점 미만이면 F 등급입니다.

    만약 점수의 1의자리가 5이상이라면
    + 등급을 추가로 부여해주세요.
    """

#q3_review(50)
#q3_review(75)

def q4_review():
    """
    단판 가위바위보를 하는 프로그램을 구현해주세요.
    사용자로부터 userA와 userB의 패를 입력받으세요
    패 : 가위 | 바위 | 보
    userA와 userB 게임결과 (승|무|패)를 출력해세요.
    """
    print ('가위! 바위! 보!')
    userA = input('userA: ')
    userB = input('userB: ')
    
    if(userA == userB):
        print('무승부입니다.')
    elif(userA == '가위' and userB == '바위'):
        print('패배입니다.')
    elif(userA == '바위' and userB == '보'):
        print('패배입니다.')
    elif(userA == '보' and userB == '가위'):
        print('패배입니다.')
    else:
        print('승리입니다.')

#q4_review()


def validate(card):
    return card == '가위' or card == '바위' or card == '보'

def q4():
    """
    단판 가위바위보를 하는 프로그램을 구현해주세요.
    사용자로부터 userA와 userB의 패를 입력받으세요
    패 : 가위 | 바위 | 보
    userA와 userB 게임결과를 userA 기준에서 (승|무|패)를 출력해주세요.
    """
    userA = input('userA 가위! 바위! 보: ')
    if(not validate(userA)):
        print('잘못된 입력값 입니다.')
        return
    
    userB = input('userB 가위! 바위! 보: ')
    if(not validate(userB)):
        print('잘못된 입력값 입니다.')
        return

    # 빠른 리턴
    # 함수를 종료할 수 있는 조건일 때 코드블록을 수행한 이후 함수를 바로 종료시키면
    # 후속 로직의 복잡도가 내려간다.
    if(userA == userB):
        print('비겼다.')
        return
    
    if(userA == '가위' and userB == '바위'):
        print('졌습니다.')
        return

    if(userA == '바위' and userB == '보'):
        print('졌습니다.')
        return

    if(userA == '보' and userB == '가위'):
        print('졌습니다.')
        return
    
    print('이겼습니다.')

# q4()



def q5():
    """사용자가 결제한 금액만큼 메세지를 출력할 수 있는 프로그램을 구현
    메세지는 건당 5000원입니다.
    출력되는 메세지 양은 아래와 같습니다.
    [id]: message (남은 결제 금액)

    결제금액은 사용자로부터 입력받습니다.
    id는 사용자로부터 입력받습니다.

    메세지를 출력하기 위한 비용이 부족하면
    '충전금액이 부족합니다.'를 출력하고 프로그램을 종료합니다.

    사용자가 비속어를 사용하면
    '비속어는 사용할 수 없습니다.'를 출력하고 입력창으로 돌아갑니다.
    이 때 비용은 부과되지 않습니다.

    비속어 사전 : '강아지', '새'
    
    쌤은 코드 12줄 나옴.
    """

    id = input('id: ')
    payment = int(input('충전금액: '))
    fee = 5000

    while(True):
        message = input('message: ')

        if(('강아지' in message) or ('새' in message)):
            print('비속어는 사용할 수 없습니다.')
            continue
        
        if(payment < fee):
            print('충전금액이 부족합니다.')
            break
        
        if(payment >= fee):
            payment -= fee
            print(f'[{id}]: {message} (잔액: {payment})')
            
#q5()



# userA와 userB의 패를 사용자로부터 입력받기 -- presentation layer

# q4()을 재사용가능한 함수형태로 바꿔보기, 함수명 : play_game -- business layer
    # 입력계층에서 받은 userA와 userB의 패를 매개변수로 전달받아서
    # 가위바위보를 수행하고 게임결과(win, lose, semi)를 반환하는 함수

# play_game 함수가 반환한 값으로 승, 무, 패 카운트 증가시키기 -- business layer

# 만약 승 또는 패 카운트가 2보다 크거나 같아지면
# 승무패 결과를 출력하고 -- presentation layer

# 프로그램을 종료하기  
