def for1():
    for i in range(0, 2):
        for _ in range(0, 5):
            print('내부리프')
        print('외부리프')
# for1()

""" 내 예상은
내부리프
내부리프
내부리프
내부리프
내부리프
외부리프
내부리프
내부리프
내부리프
내부리프
내부리프
외부리프
"""

def for2():
    for i in range(0, 2):
        for n in range(0, 3):
            print({n},'내부리프')
    print('외부리프')
# for2()
"""
내 예상은   실제출력은
내부리프    내부리프
내부리프    내부리프
내부리프    내부리프
내부리프    내부리프
내부리프    내부리프
내부리프    내부리프
외부리프    외부리프
외부리프
"""
# for문 안에 프린트 출력하려면 들여쓰기로 하나 넣어야함.
# 이건 두 번 순환되는 for문이 모두 출력되고 외부리프가 한번 찍히는거니까
# 당연히 출력값처럼 찍힘!!

def for3():
    for i in range(0, 2):
        for n in range(0, 2):
            print({n},'내부리프')
            print('외부리프')
#for3()

def for4():
    inp = int(input('몇 번 반복?: '))
    for i in range(0, inp):
        for _ in range(1, inp+1):
            print('내부', end='')
        print('외부')
#for4()

"""
3넣으면 
내부내부내부외부    
내부내부내부외부
내부내부내부외부
"""

def a():
    inp = int(input('일반 밑변의 길이: '))
    for i in range(0, inp+1):
        for _ in range(0, i):
            print('*',end='')
        print()
#a()

# 첫 번째 반복(i = 0)에서 내부 루프는 실행되지 않습니다.
# range(0, 0)이므로 내부 루프가 실행되지 않고 바로 print()로 줄바꿈만 발생합니다.
# 결과적으로 출력의 첫 줄은 빈 줄이 됩니다.


def right():
    inp = int(input('오른쪽 직각 및변: '))
    blank = inp - 1
    for i in range(1, inp+1): # 공백 반복문
        print(' ' * blank, end=' ')
        print('*' * i, end=' ')         
        print()
        blank = blank - 1
    
    
right()


