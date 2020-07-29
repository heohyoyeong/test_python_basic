## 문제 3.
## 알파벳 대소문자로 된 문자열이 주어지면,
## 이 문자열에서 가장 많이 사용된 알파벳이
## 무엇인지 출력하는 프로그램을 작성하시오.
## 단, 대소문자는 구별하지 않아요. 만약 동률이 존재하는 경우
## 알파벳 순으로 제일 앞에 있는
## 문자를 출력하세요.

## 문자열) "This is a sample Program mississippi river"   =>  I
## 문자열) "abcdabcdababccddcd"                              => C
################################################

a="abcdabcdababccddcd"


b=list()

b.append(a.count("a"))
b.append(a.count("b"))
b.append(a.count("c"))
b.append(a.count("d"))

print(b)