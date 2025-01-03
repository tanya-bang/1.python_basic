"""
자료구조 : 대량의 데이터를 관리하는 구조

sequence : 공통시퀀스 연산, 함수를 구현
    mutable : list
    immutable : tuple, str

list : 
순서가 보장되고 중복을 허용하는 자료구조
변경 가능한(mutable) 객체 = 가변 시퀀스

데이터를 다루는 4가지 방법
CRUD #어떤데이터를 만났을 때 아 나 CRUD를 할 줄 알아. 라고 한다면 기본적인 데이터 다루는 법은 아는 것.
    C : create
    R : read
    U : update
    D : delete
"""

def list_create():
    """ 여러개의 데이터를 하나의 이름(변수)로 다루기 위한 객체
        순서가 보장되고 중복을 허용하는 자료구조
    """

    #모든 타입을 요소로 가질 수 있다.
    a = [1, 'a', True, [1,2,3]]
    a.append(1000) #리스트 추가
    print(a)

    #그런데 맨 뒤 말고, a의 3번인덱스 뒤에 'python'을 추가해야한다면...?
    a.insert(3, 'python')
    print(a)

list_create()

def list_read():
    # a가 가지고 있는 위치 + index * 데이터의 크기
    a = [1, 2, 3, 4]

    # list안의 데이터는 index를 통해 접근할 수 있다.
    # index는 0부터 list안에 들어있는 요소의 개수 -1까지 순차적으로 증가하는 수열

    index0 = a[0]
    print(index0)

    # list안에 들어있는 요소(element)를 반복문을 사용해 확인
    for e in a:
        print(e**2, end=' | ')

def list_update():
    a = [1, 2, 3, 4]
    a[2] = 100 #2자리(첫번째 이후 2자리라 세번째에 있는 데이터를 100으로 바꾸겠다는 뜻
    print(a)

def list_delete():
    a = [1, 2, 3, 4]
    del a[3]
    print(a)

list_read()
#list_update()
#list_delete()