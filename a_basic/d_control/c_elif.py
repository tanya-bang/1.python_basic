"""
다중조건문

if(c):
else:
    if(c):
    else:
        if(c):
        else
이런 경우가 생긴다면 (코드블럭 안에 코드블럭이 중첩되는 것을 코드인덴트라고 부르는데)
이 인덴트가 없어야 좋은 코드라고 한다.

if(c):
elif(c):
else:
"""

def study_elif(score):
    """
    매개변수로 점수를 전달 받아 등급을 출력하세요
        90점 이상이면 A
        80점 이상 90점 미만이면 B
        70점 이상 80점 미만이면 C
        60점 이상 70점 미만이면 D
        60점 미만이면 F 로 등급입니다.
    """
    if(score >= 90):
        print('A')
    elif(score >= 80):
        print('B')
    elif(score >= 70):
        print('C')
    elif(score >= 60):
        print('D')
    else:
        print('F')

    # 문제를 그대로 옮기면 score <90 and score >= 80라고 쓸 수 있겠지만
    # 이미 첫번째 if가 실행이 안되고 밑의 elif로 들어온다면 이미 90점 미만이라는 거니까
    # score >= 80만 남아도 되는 것.

study_elif(75)
