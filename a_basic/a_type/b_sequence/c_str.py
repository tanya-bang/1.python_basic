"""
문자열 : 문자(글자)의 배열
        :문자를 요소로 가지는 불변 시퀀스
"""

def str_read():
    msg = '몰랐죠? 사실 문자열도 시퀀스에요'
    print('사실' in msg)
    print('작:', min(msg), '큰:', max(msg))#아스키코드에서 디코딩-인코딩되는 거겠지.
    print(msg[3])

    for e in msg:
        print(e)

str_read()
