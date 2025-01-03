from error.errors import *
from random import randrange

class NaverAPI:
    def __init__(self, timeout:int):
        if(timeout < 0):
            raise IllegalPropertyError
        
        self.__timeout = timeout
        
    def connect(self):
        delay = randrange(1,10)
        
        if(delay > self.__timeout):
            raise TimeoutError
        
        print(f'네이버 서버에 연결되었습니다. 소요시간: {delay}')
