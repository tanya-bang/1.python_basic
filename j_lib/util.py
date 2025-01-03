import re

def check_re(pattern, text, flag=0):
    matched = re.search(pattern, text, flag)
    if(matched):
        print(f'{pattern}:; {matched.group()}')
    else:
        print(f'{pattern}: not found!')
    
    # 이 함수 이해가 안감.... 