
# first class

# first-class citizen(1급 시민)

# 프로그램의 구성요소(개체-값, 객체, 함수)가 다음의 조건을 만족하면
# first-class citizen이라고 불러요!!

# 1. 구성요소가 변수나 데이터 구조의 속성으로 저장될 수 있어요!
# 2. 함수의 인자로 전달될 수 있어요!
# 3. 함수의 결과로 리턴될 수 있어요!

# 아주 쉽게 생각하면
# 우리가 사용하는 일반 숫자 타입의 데이터 => 변수에 저장도 가능하고
# 함수의 인자로 넘겨줄 수 있고 함수의 결과로 리턴될 수 있어요!!
# 일반 숫자는 일급시민입니다.!!

# 우리가 사용하는 객체(class로 부터 파생된 instance)
# python에서 사용되는 객체는 1급시민의 조건을 만족해요 => 1급 객체

# python의 함수는 어떻게 될까요???
# 만약 1급 시민의 조건을 만족한다면 일급 함수(first class function)하고
# 불러요!!
# python은 일급함수를 지원하는 언어예요!!
# => 함수를 runtime으로 생성할 수 있어요!

# 1. 함수를 변수에 저장할 수 있어요!

# def my_add(x,y):
#     return x + y
#
# print(my_add)
#
# f = my_add
#
# print(f(100,200))

# 2. 함수를 다른 함수의 인자로 전달할 수 있어요!

# def my_add(x,y):
#     return x + y
#
# def my_sub(x,y):
#     return x - y
#
#
# def my_operation(func, arg_list):
#     result = []
#
#     for (tmp1,tmp2) in arg_list:
#         result.append(func(tmp1,tmp2))
#
#     return result
#
#
# data = [(1, 2), (3, 4), (5, 6)]
#
# print(my_operation(my_sub,data))

# 3. 함수를 다른 함수의 리턴값으로 사용할 수 있어요!
#    => Closure라는 개념도 같이 이해해야 해요!

def addMaker(x):   # x는 지역변수로 함수가 호출되면 생성되고 함수가 종료되면 없어져요!!

    def my_add_maker(y):
        return x + y

    return my_add_maker

add_5 = addMaker(5)
add_10 = addMaker(10)

print(add_5(100))
print(add_10(100))

###############################################

# Closure
# first class function(일급함수)의 개념을 이용하여
# 스코프에 묶인 변수를 바인딩 하기 위한 기술을 의미해요!
# 클로저는 데이터를 저장한 레코드예요. 스코프안의 변수가
# 소멸되어도 그에 대한 접근을 클로져를 통해서 할 수 있어요!

# 클로져의 도움을 받아 런타임시에 내가 필요한 함수를
# 만들어 낼 수 있어요!!




