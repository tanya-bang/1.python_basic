def fnc1():
    """
    a = [1, 'a', True, [1,2,3]]
    b = [1.1, None]
    두 리스트를 합쳐 c 변수에 할당하세요.
    """
    a = [1, 'a', True, [1,2,3]]
    b = [1.1, None] 
    c = a + b
    print (c)   
fnc1()

def fnc2():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    a의 1,3,5 인덱스의 요소를 요소로 가지는 list를 구하세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    newa = [a[1], a[3], a[5]]
    print(newa)
fnc2()

def fnc3():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None] 의
    길이를 구하시오.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print(len(a))
fnc3()

def fnc4():
    """
    a = [30, 8, 900, 77, -9, 100]
    a의 가장 작은 요소와 가장 큰 요소의 합을 구하시오.
    """
    a = [30, 8, 900, 77, -9, 100]
    print(min(a) + max(a))
fnc4()

def fnc5():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 순서를 뒤집으세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    a.reverse()
    print(a)

fnc5()


def fnc6():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 0, 2, 4 인덱스의 요소를 -999로 대체하세요.
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    a[0] = -999
    a[2] = -999
    a[4] = -999
    #a[0:5:2] = [-999, -999, -999]
    print(a)
   
fnc6()

def fnc66():
    a = [1, 'a', True, [1,2,3], 1.1, None]
    print('슬라이스: ', a[0:5:2])
    a[0:5:2] = [-999, -888, -777]
    print('fnc66: ', a)
fnc66()

def fnc7():
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    의 복사본을 만들어 b에 할당하시오
    """
    a = [1, 'a', True, [1,2,3], 1.1, None]
    b = a.copy()
    print(b)
fnc7()

def copy():
    starbucks = ['아메리카노', '카페라떼', '프라푸치노']
    print('starbuks', starbucks)

    bbaeck = starbucks
    bbaeck.append('식혜')
    print('bbaeck', bbaeck)

    print('?', starbucks)
    #아무것도 안하고 앞에서 빽다방에만 식혜를 추가했는데 왜 갑자기 스타벅스에 식혜가 추가됐어?!
    #stack 메모리와 heap 메모리 때문에 / 현재 스타벅스와 빽다방에 할당되어있는 주소가 똑같음
    print('스벅주소:',id(starbucks))
    print('빽주소:', id(bbaeck))
    
    #그래서 이 불상사를 피하기 위해서는
    #bbaeck에 복사하는 starbucks.copy()를 활용해야함 (=참조개념)
    bbaeck = starbucks.copy()
    bbaeck.append('수정과')
    print('빽:', bbaeck)
    print('스타벅스: ', starbucks)

copy()
