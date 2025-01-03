"""
등위비교(==)일 때 사용하는 제어문
"""
def study_match(status):
    match status:
        case 400:
            print('Bad request')
        case 401 | 402:
            print('Not allowed')
        case 404:
            print('Not found')
        case 418:
            print('Im a teapot')
        case _:#위의 case에 등록되지 않은 다른 숫자인 경우
            print('등록되지 않은 상태코드 입니다.')
        #이거 뭐예요? if/elif죠. 근데 대신 비교가 =인. (switch case 문이라고 하기도함

study_match(300)