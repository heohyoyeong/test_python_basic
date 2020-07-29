# first class

# first-class citizen (1급시민)

# 프로그램의 구성요소(개체-값, 객체(instance), 함수)가 다음의 조건을 만족하면 first-class citizen이라 부른다.

# 1. 구성요소가 변수나 데이터 구조의 속성으로 저장될 수 있다.

# 2. 함수의 인자로 전달될 수 있다.

# 3. 함수의 결과로 리턴될 수 있다.

# 아주 쉽게 생각하면
# 우리가 사용하는 일반 숫자 타입의 데이터 => 변수에 저장가능, 함수의 인자로 넘겨 줄 수 있고, 함수의 결과로 리턴 가능 => 숫자는 1급시민

# 우리가 사용하는 객체(class로 부터 파생된 instance)
# 파이썬에서 사용되는 객체는 1급시민의 조건을 만족한다. => 1급 객체

# python은 1급함수를 지원하는 언어이다.
# 만약 1급시민의 조건을 만족한다면 1급 함수(first class function)라 부른다. => 함수를 runtime으로 생성할 수 있다.

# 1. 함수를 변수에 저장할수 있다.

# def my_add(x,y):
#     return x + y
#
# print(my_add)
# f=my_add
# print(f(100,200))

# 2. 함수를 다른 함수의 인자로 전달할 수 있다.

# def my_add(x,y):
#     return x+y
#
#
# def my_sub(x,y):
#     return x-y
#
# def my_opperation(func,arg_list):
#     result =[]
#     for (tmp1,tmp2) in arg_list:
#         result.append(func(tmp1,tmp2))
#     return result
#
# data=[(1,2),(3,4),(5,6),(7,8)]
# print(my_opperation(my_add,data))
# print(my_opperation(my_sub,data))

# 3. 함수를 다른 함수의 리턴 값을 사용할수 있어요.
#   => closure라는 개념도 같이 이해해야한다.

# def addMaker():
#
#     def my_add_maker():
#         return 100
#
#     return  my_add_maker
#
# print(addMaker()())
# print(addMaker())

# tmp1= 100
#
# def my_func(): #매게변수도 지역변수다!
#     tmp2=200
#     return tmp2
#
# print(tmp1) # 100
# my_func()
# print(tmp2) #지역변수라서 안된다! 이말이야 에러뜬다! 이말이야

# def addmaker(x): #x는 지역변수, 함수가 호출되면 생성되고 종료되면 없어진다.
#     def my_addmaker(y):
#         return x+y
#
#     return my_addmaker
#
# add_5=addmaker(5)
# add_10=addmaker(10)

# print(add_10(100))
# print(add_5(100))
#############################################################################

# Closure
# first class function(1급함수) 개념을 이용하여 scope에 묶인 변수를 바인딩 하기 위한 기술이다. ????
# 지역변수를 나중에 사용하기 위한 것이다..
# closure는 데이터를 저장한 레코드..
# 스코프안의 변수가 소멸되어도 그에 대한 접근을 클로져를 통해서 할 수 있다.
# closure의 도움으로 runtime시에 내가 필요한 함수를 만들어 낼 수 있다.
