from random import randrange
import traceback

def study_error():
    while(True):
        inp = input('1 숫자: ')
        if(inp == 'exit'):
            break
        
        if(not inp.isnumeric()):
            print('숫자를 입력하세요')
            continue
        
        # 예외처리 1. 로직을 잘 작성한다.
        if(inp == '0'):
            print('0은 안돼')
            continue
        
        num = int(inp)
        random = randrange(1, 10)
        print(f'{random}/{num} = {random/num}')

#study_error()

def study_error2():
    """
    try - except
    try블록에서 except에 지정한 예외가 발생했을 때,
    프로그램을 멈추는 대신
    except 블록에 지정한 코드를 실행
    """

    while(True):
        try:
            inp = input('2 숫자: ')
            if(inp == 'exit'):
                break
            
            if(not inp.isnumeric()):
                print('숫자를 입력하세요')
                continue
            
            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')
            
        except ZeroDivisionError as e:
            print('0은 입력할 수 없습니다.')
            print('예외메시지:', e)
            
        except ValueError:
            print('숫자를 입력하세요.')
            
study_error2()


def study_error3():
    while(True):
        try:
            inp = input('3 숫자: ')
            if(inp == 'exit'):
                break
                       
            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')
            
        except Exception:
            print('예외가 발생했습니다.')
            
#study_error3()

def study_error4():
    while(True):
        try:
            inp = input('4 숫자: ')
            if(inp == 'exit'):
                break
                       
            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')
            
        except:
            print('예외가 발생했습니다.')
        finally:
            # 예외 발생여부와 무관하게 반드시 실행되는 코드
            print('======================')
            
#study_error4()

def study_error5():
    while(True):
        try:
            inp = input('5 숫자: ')
            if(inp == 'exit'):
                break
                       
            num = int(inp)
            random = randrange(1, 10)
            print(f'{random}/{num} = {random/num}')
            
        except:
            print('예외가 발생했습니다.')
            # traceback을 import 한 다음
            traceback.print_exception
        finally:
            # 예외 발생여부와 무관하게 반드시 실행되는 코드
            print('======================')
            
#study_error5()