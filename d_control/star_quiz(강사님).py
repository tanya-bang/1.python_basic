def q1():
    width = int(input('너비: '))
    height = int(input('높이: '))

    for _ in range(0, height):
        for _ in range(0, width):
            print('*', end='')
        print()

def q2():
    """ 사용자로부터 입력받은 구구단을 출력하시오
    """
    dan = int(input('몇 단: '))
    for n in range(1,10):
        print(f'{dan} * {n} = {dan*n}')


def q3():
    """ 2단부터 9단까지 구구단을 출력하시오.
    """

# 난이도 상
def q4():
    """ 2단부터 9단까지 구구단을 출력하시오.
    가로방향으로 출력하시오.
    """

def q5():
    """ 사용자가 입력한 너비와 높이의 직각삼각형을 그리세요.
        직각은 밑변의 좌측에 위치합니다.
    ex) 4 * 4
        *
        **
        ***
        ****
    """
    inp = int(input('밑변의 길이: '))
    for n in range(1, inp+1):
        for _ in range(0, n):
            print('*', end='')
        print()
q5()
    



def q6():
    """ 사용자가 입력한 너비와 높이의 직각삼각형을 그리세요.
        직각은 밑변의 우측에 위치합니다.
    ex) 4 * 4
           *
          **
         ***
        ****
    """
    

# 난이도 상
def q7():
    """ 한 변의 길이가 사용자의 입력값인 다이아몬드를 그리세요
    ex) inp = 5
             *
		    ***
		   *****
		  *******
		 *********
		  *******
		   *****
		    ***
		     *
    """
