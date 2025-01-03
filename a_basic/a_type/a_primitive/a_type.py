#모든 수식은 숫자 또는 논리(T/F)로 표현될 수 있어야 한다.

print('hello world')

""" literal 확인
literal : 직접 표현된 값, 변수에 할당되지 않은 값
"""

print(1) 
print(1.1)
print(True)
print(False)
print('hi world')


""" type
type : 형태, 모양
type() : ()안에 들어오는 인자의 타입을 반환-괄호 안에 들어오는 애를 "인자"라고 함
"""
print(type(10)) #int (정수타입이구나
                    #meaning that: 컴터야 네가 2진수로 저장한 데이터를 정수 형태로 볼거야!라고 말하는 것)
print(type(10.1)) #float (실수타입이구나)
print(type(True)) #bool (불리언타입이구나)
print(type(False)) #bool
print(type('hello world')) #str (문자열이라는 타입이구나)


print("""
형변환
""")
print(float(10))
print(int(10.3))
print(int(True))
print(ord('h')) #해당 문자의 문자코드표 순서


print("""
숫자를 문자로 인코딩한 값
""")
# encoding : 데이터를 특정한 형식으로 변경
# decoding : encoding된 데이터를 본래 형식으로 변경
# ex) 010-3329-3364 -> 010-xxxx-xx34 (본래의 데이터를 특정한 형식으로 변경했으니 encoding)
print(chr(104))


print("""
파이썬은 객체의 boolean 변환을 지원해준다.
str => 빈 문자열이면 False
int, float => 0이면 False
None => False
""")

print(bool(0))
print(bool(100))
print(bool(''))
print(bool('aaaa'))
print(bool(None))