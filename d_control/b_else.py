"""양자택일 조건문
if(조건식):
    코드블록
else:
    코드블록
"""

def study_else(arg):
        """매개변수로 전달된 정수가 짝수? 홀수?"""
    
        if(arg % 2 == 0):
            print('짝수입니다.')
        else:
            print('홀수입니다.')
study_else(33)
