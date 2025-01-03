"""
date : 날짜를 다루는 모듈
datetime: 날짜와 시간을 다루는 모듈
"""
from datetime import *

def study_date():
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    print(today)
    print(f'{year}년 {month}월 {day}일')
    
    xmas = date(2024, 12, 25)
    # 공식문서에서 이렇게 쓰래~
    print(xmas)
#study_date()

def study_datetime():
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day
    hour = today.hour
    minute = today.minute
    second = today.second
    print(f'{year}년 {month}월 {day}일')
    print(f'{hour}시 {minute}분 {second}초')
    
    christmas = datetime(2024, 12, 25)
    print(christmas)
#study_datetime()

def study_timedelta():
    now = datetime.now()
    print(now)
    print(now + timedelta(days=-1))
    print(now + timedelta(days=2))
    print(now + timedelta(days=5, hours=3))
#study_timedelta()

# 사용자로부터 yyyy-mm-dd 양식으로 입력받은 날짜가
# 오늘로부터 며칠 남았는지, 혹은 지났는지 계산하는
# D-day 계산기
def d_day():
    inp = input('날짜(yyyy-mm-dd) : ')
    d_day = date.fromisoformat(inp)
    today = date.today()
    cal = d_day - today
    
    print(f'{d_day}까지 {cal.days}일 남았습니다.')

d_day()