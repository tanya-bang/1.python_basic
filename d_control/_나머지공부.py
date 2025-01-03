# 걍 연습
def study_break():
    id = input('id: ')
    
    while True:
        message = input('message: ')
        print(f'[{id}]: {message}')

        if message == '바보':
            print('금칙어는 쓸 수 없습니다.')
            continue  # 현재 반복 중단, 루프 처음으로 돌아감

        if message == 'exit':
            print('채팅앱을 떠나셨습니다.')
            restart = input('다시 시작하시겠습니까? (yes/no): ')
            if restart.lower() == 'yes':
                id = input('id: ')  # 새로운 ID 입력
                continue  # 현재 반복 중단, 루프 처음으로 돌아감
            else:
                print('프로그램을 종료합니다.')
                break  # 루프 완전히 종료


def study_break():
    id = input('id: ')
    
    while True:
        message = input('message: ')
        print(f'[{id}]: {message}')

        if message == '바보':
            print('금칙어는 쓸 수 없습니다.')
            continue  # 루프를 처음으로 돌아감

        if message == 'exit':
            break  # 루프를 완전히 종료

    print('채팅앱을 떠나셨습니다.')




def study_extra():
    while True:
        study_break()  # study_break 함수 호출
        restart = input('다시 시작하시겠습니까? (yes/no): ')
        if restart.lower() != 'yes':  # "yes"가 아니면 종료
            print('프로그램을 종료합니다.')
            break
#study_extra()

def study_e2():
    id = input('id: ')
    
    while True:
        message = input('message: ')
        print(f'[{id}]: {message}')
        

        if message == '바보':
            print('금칙어는 쓸 수 없습니다.')
            continue  # 현재 반복 중단, 루프 처음으로 돌아감

        if message == 'exit':
            print('채팅앱을 떠나셨습니다.')
            restart = input('다시 시작하시겠습니까? (yes/no): ')
            if restart.lower() == 'yes':
                id = input('id: ')  # 새로운 ID 입력
                continue  # 현재 반복 중단, 루프 처음으로 돌아감
            else:
                print('프로그램을 종료합니다.')
                break  # 루프 완전히 종료

def example():
    while True:
        print("안녕하세요")
        break  # 루프 종료, 함수 실행은 계속 진행
    print("루프 종료")  # 실행됨

example()
    # 출력화면 :
    # 안녕하세요
    # 루프 종료

def example():
    while True:
        print("안녕하세요")
        return  # 함수 종료, 아래 코드는 실행되지 않음
    print("루프 종료")  # 실행되지 않음

#example()
