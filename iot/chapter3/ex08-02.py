# .isalpha : 모든 문자가 알파벳인가?
# .islower : 모든 문자가 소문자인가
# .isupper : 모든 문자가 대문자인가
# .isspace : 모든 문자가 공백인가
# .isalnum : 모든 문자가 숫자혹은 알파벳인가
# .isdecimal : 모든문자가 숫자인가
# .isdigit : 모든문자가 숫자인가
# .isnumeric : 모든문자가 숫자인가
# .isidentifier : 명칭으로 설정가능
# .isprintable : 프린트 가능

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
#
# s = "Good morning. my love KIM."
# s2= "서울->대전->대구->부산"
# print(s.split())
# print(s2.split("->"))
# a=s.split()
# b=s.splitlines()
# d=" ".join(a)
# print(d)
# print(b)

# def main():
#     s='Good morning. my love kim.'
#     print(s.lower()) #전부 소문자로
#     print(s.upper()) # 전부 대문자로
#     print(s.swapcase()) # 대문자는 소문자로, 소문자는 대문자로 변환
#     print(s.capitalize()) # 첫글자는 대문자 나머지는 모두 소문자로 변환
#     print(s.title()) # 모든 단어의 첫 글자를 대문자로 나머지는 소문자로 변환
#     print(s)

# trabler ="""
# 강나루 거너서
# 밀밭 길을
#
# 구름에 달 가듯이
# 가는 나그네
# """
# poet = trabler.splitlines()
# print(poet)

# s="._."
#
# print(s.join("대한민국"))
#
# print("._.".join("대한민국"))

