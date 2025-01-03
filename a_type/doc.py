"""
backus-Naur form 문법
프로그래밍 언어의 구문을 설명하기 위해 사용하는 표기법

기호 ::= ___표현식___

| : 또는
eg_ 
lc_letterlc_letter / lc_letter_ / lc_letter 모두 가능하다는 뜻

* : 0번 이상
+ : 1번 이상
[] : 0번 또는 1번
() : 표현식을 그룹으로 묶을 때 사용
"" : 문자열 ex) "for"
문자...문자 : 코드표상 문자 사이에 존재하는 문자가
        eg) a...d, => b,c
<> : 다른 기호로 확장될 수 있음

    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    number ::= <digit>+
            meaning that:뭐 아무렇게나 올 수 있단 뜻. 0뒤에1 1뒤에234 (???)

name ::= lc_letter(lc_letter|"_")*
lc_letter ::= "a"..."z"
라면, name은 lc_letter가 반복될 수도 있고 반복되지 않을 수도 있다.
즉 name : 알파벳과 _로만 구성된 문자열
            
"""