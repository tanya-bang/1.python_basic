""" 
q1. 변수 x와 y에 담긴 값을 서로 바꿔주세요.
단, x, y 변수에 리터럴을 할당하는 방법은 안됩니다.
"""
x, y = 100, 200

z = x
x = y
y = z

# x, y = y, x
print(x) #200
print(y) #100