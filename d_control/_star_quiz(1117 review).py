"""
****
****
****
****
"""
def q1():
   for n in range(0, 4):
        for i in range(0,4):
                print('*', end='') # end에 아무것도 안넣으면 \n처리되어서 줄바꿈이 되는데 우리는 지금 
        print()
#q1()

"""
사용자로부터 너비와 높이를 받아서 라는 말이 들어가면
"""

def q1_1():
    width = int(input('너비 : '))
    height = int(input('높이 : '))
    for n in range(0, height):
        for i in range(0,width):
                print('*', end='') # end에 아무것도 안넣으면 \n처리되어서 줄바꿈이 되는데 우리는 지금 
        print()
#q1_1()

def q2():
    """사용자로부터 입력받은 구구단을 출력하시오.
    """
    want = int(input('몇 단? : '))
    for i in range(1,10):
        result = want * i
        print(f'{want} * {i} = {result}')
        result = want
    # 굳이 result로 저장할 필요가 없다.
    # 그냥 for문 바로 밑에 print하면 변수로 저장 안하니까 값이 바뀌지도 않고
    # 값이 안바뀌니까 맨 밑줄도 필요 없게되자나!!


#q2()

def q3():
    """2단부터 9단까지 구구단을 출력하시오.
    """
    for dan in range(2,10): 
        for i in range(1,10):
            result = dan * i
            print(f'{dan} * {i} = {result}')
        print('----------------')
#q3()


def q4():
    """2단부터 9단까지 구구단을 출력하시오.
     가로방향으로 출력하시오.
    """
    for dan in range(1,10): 
            for i in range(2,10):
                result = i * dan
                print(f'| {i} * {dan} = {result:2} |', end='')
            print()
#q4()

def q5():
    """ 사용자가 입력한 너비와 높이의 직각삼각형을 그리세요.
        직각은 밑변의 좌측에 위치합니다.
    ex) 4 * 4
        *
        **
        ***
        ****
    """
    while(True):
        width = int(input('너비 : '))
        height = int(input('높이 : '))

        if (width != height):
            print('직각삼각형을 출력하기 위해서는 너비와 높이가 같아야합니다.')  
            continue

        for n in range(1, width +1):
            print('*' * n)
        break
        
#q5()

def q5_test():
    width = int(input('밑변 입력'))
    for n in range(1, width +1):
        print('*' * n)
#q5_test()


def q6():
    """ 사용자가 입력한 너비와 높이의 직각삼각형을 그리세요.
        직각은 밑변의 우측에 위치합니다.
    ex) 4 * 4
           *
          **
         ***
        ****
    """
q6()



def q6_reverse_test():
    while(True):
        width = int(input('reverse 너비 : '))
        height = int(input('reverse 높이 : '))

        if (width != height):
            print('직각삼각형을 출력하기 위해서는 너비와 높이가 같아야합니다.')  
            continue

        for n in range(width, 0, -1):
            print('*' * n)
        break
q6_reverse_test()

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