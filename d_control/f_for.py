"""
for문
특정 횟수를 반복하는 반복문을 안전하게 작성할 수 있게 도와주는 문법
"""
def study_for():
    # i : 0, 1, 2, 3, 4
    for i in range(0, 5):
        print(i, '안녕파이썬')

def study_for_sum():
    """ 1부터 10까지 정수들의 합계를 구하시오.
        1. 반복문을 사용한다 (for)
        2. 4의 배수는 합계를 구할 때 제외한다.
    """
    #1부터 10까지 합계를 구하기 어려우면 1부터 10까지 찍어보는 것부터 출력
    
    sum = 0
    for i in range(1, 11):
        if(i % 4 != 0):
            sum = sum + i #sum += i 로 표현 가능
    else:
        print(sum)

study_for_sum()


def q6():
    inp = int(input('밑변의 길이: '))
    for n in range(1, inp+1):
        for _ in range(0, inp - n):
            print(' ', end='')
        for _ in range(0, 1 + 2*(n-1)):
            print('*', end='')
        print()


def q1():
    width = int(input('너비: '))
    height = int(input('높이: '))

    for _ in range(0, height):
        for _ in range(0, width):
                print('*', end='')
        print()

