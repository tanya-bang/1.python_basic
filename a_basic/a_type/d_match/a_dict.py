"""
dict : key-value 형태로 데이터를 관리하는 자료구조
key : 식별자, 유일한 값
value : 저장할 데이터, 중복을 허용한다.
"""
    # 어떤점이 좋을까?
    # 이름을 붙여주면 그 데이터가 어떤 의미를 가지는지 알 수 있었듯이 동일한 효과를 낸다.
    # key에 해당하는 부분은 굳이 문자열일 필요 없이

def study_dict():
    origin = {"one":1, "two":2, "three":3, "age":45}
    a = dict(one=1, two=2, three=3)

    region = ['서울', '대구', '부산']
    population = [100, 300, 500]

    #따로 들어온 데이터를 취합해서 하나의 데이터로 만드는게 우리가 하는 일이잖아요?

    c = dict(zip(region, population))

    print(c)
    print(origin['three'])
    
    print(origin['age'])
    print(c['대구'])

    # C (Create in CRUD)
    origin['four'] = 4
    print(origin)
    
    # R
    # key-value 쌍으로 읽기
    for entry in origin.items():
        print(entry)
        print(type(entry)) # => 불변시퀀스인 tuple로 묶였넹

    # key 만 확인 가능
    for key in origin.keys():
        print(f'[key만 확인]:{key}')
   

    for key in origin.keys():
        if('t' in key):
            print('[t포함?:]', key)
            print('[t포함?:]', origin[key])
             # key 값에 t가 포함된 애들만 뽑아서 보고싶은데?
            # 강의에서 print(origin[key])로 하라고 알려주셨는데 그렇게하면 안나옴 ㅠ
            # ==> 강의에서 알려준거 적용하면 키가 아닌 value를 호출하는 기능이라 2,3이 출력됨

    # value 만 확인 가능
    for v in origin:
        print('value만: ', v)

    # key값으로 특정 요소를 식별
    print(origin['one'])

    # U
    origin['one'] = '하나'

    # D
    del origin['one']
    print(origin)


study_dict()

