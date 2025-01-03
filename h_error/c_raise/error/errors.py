# 예외로 다루기 위한 클래쓰를 만들겠습니다.
class IllegalPropertyError(Exception):
    # 얘를 예외로 다루기 위해서는 exception 클래스를 상속받으면 된다.
    def __init__(self, msg='부적절한 값입니다.'):
        self.msg = msg
    #__하면 캡슐화 하는건가봐 self.__msg 했다가 캡슐화하지 맙시다. 하면서 __를 지움.
    
    def __str__(self):
        return self.msg
    # 매직메서드 써보기?
    # 이 객체(클래스)를 문자열로 나타낸다면...
    
class TimeoutError(Exception):
    def __str__(self):
        return '통신지연이 발생했습니다.'
    # 객체를 넘겼을 때 객체가 반환하는값을 보고싶을 때 str을 호출
    # 아까 배운 오버라이드 개념이 나오는듯 
 
