# .isalpha : 모든 문자가 알파벳인가?
# .islower : 모든 문자가 소문자인가
# .isupper : 모든 문자가 대문자인가
# .isspace : 모든 문자가 공백인가
# .isalnum : 모든 문자가 숫자혹은 알파벳인가
# isdecimal : 모든문자가 숫자인가
# isdigit : 모든문자가 숫자인가
# isnumeric : 모든문자가 숫자인가
# isidentifier : 명칭으로 설정가능
# isprintable : 프린트 가능

# .lower() :전부 소문자로
# .upper() : 전부 대문자로
# .swapcase() : 대문자는 소문자로, 소문자는 대문자로 변환
# .capitalize() : 첫글자는 대문자 나머지는 모두 소문자로 변환
# Good morning. my love kim.
# .title(): 모든 단어의 첫 글자를 대문자로 나머지는 소문자로 변환
# Good Morning. My Love Kim.
# .strip() : 좌우에 있는 공백을 제거
# .lstrip(): 왼쪽에 있는 공백을 제거
# .rtrip(): 오른쪽에 있는 공백을 제거

s = "Good morning. my love KIM."
s2= "서울->대전->대구->부산"
print(s.split())
print(s2.split("->"))


f=123.123145

print("####%-20f###"%f)
print("####%2d###"%f)