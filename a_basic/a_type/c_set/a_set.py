"""
set(집합) : 중복을 허용하지 않고 순서가 없는 자료구조
set : mutable 객체
frozen_set : immutable 객체

"""

def study_set():
    set_a = {'백지영', '윤도현', '김경호', '김경호'}
    set_b = {'김경호', '라나델레이', '아델', '박정현'}
    set_c = {'김경호', '백지영'}

    # C
    set_a.add('로제')

    # R 
        # list에서는 index로 했었음 그러나 set에서는 불가능
            # for로 안에 있는 애들을 통째로 들고와야함
    for e in set_a:
        print('a집합: ', e)
        
    # U >>> 지원안됨 // set_a라는 집합을 수정하는 것.
    #   수정을 위해서는 식별자가 필요하다.
    #   a list의 3번 인덱스에 있는 값을 '파이썬'으로 변경
    #   key 값이 'mc'인 학원의 이름을 변경
    #  set은 요소를 특정할 수단이 없기 때문에 수정이 없음
    #   김경호를 지우고 김연우를 넣는다고 해서 수정이 되는 개념은 아님 

    # D
    set_a.remove('로제')
    print(set_a)

study_set()