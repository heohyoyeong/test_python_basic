# Decorator

# Decorator의 사전적의미는 장식가, 도배업자
# python에서 Decorator는 기존의 코드에 여러가지 기능을 추하는 python구문이라고 이해하면 됨

# closure
# first class에 대하여 알아보았다.
# first class function(1급함수) : python은 1급함수를 지원하는 언어
# 1. python의 함수는 변수에 저장이 가능하다.
# 2. 함수의 인자로 함수를 이용할 수 있다. ==> Decorator
# 3. 함수의 결과 값(return)으로 함수를 이용할 수 있다. ==> closure

# def my_outer_func(func):
#
#     def my_inner_func():
#         func()
#
#     return my_inner_func
#
# def my_func():
#     print("my_func() 함수가 호출되었어요!")
#
# decorated_my_func=my_outer_func(my_func)
# decorated_my_func()
# my_func()
#########################################################################
# import time
#
# def my_outer_func(func):
#
#     def my_inner_func():
#         print("{} 함수수행시간을 계산합니다.".format(func.__name__))
#         start= time.time() #1970년 1월 1일 0시 0분 0초가 0이고 1초가 1
#         func()
#         end= time.time()
#         real_time= print(f"함수 수행 시간은 {start-end}초입니다.")
#
#     return my_inner_func
#
# def my_func():
#     print("my_func() 함수가 호출되었어요!")
#
# decorated_my_func=my_outer_func(my_func)
# decorated_my_func()
# #####################################################################
# import time
#
# def my_outer_func(func):
#
#     def my_inner_func():
#         print("{} 함수수행시간을 계산합니다.".format(func.__name__))
#         start= time.time() #1970년 1월 1일 0시 0분 0초가 0이고 1초가 1
#         func()
#         end= time.time()
#         real_time= print(f"함수 수행 시간은 {start-end}초입니다.")
#
#     return my_inner_func
#
#
# @my_outer_func # my_func()은 my_outer_func에 넣어서 사용한다! 라고 선언한다. 대박.. @를 쓴다는 것이 decorator
# def my_func():
#     print("my_func() 함수가 호출되었어요!")
#
# my_func()
#
##########################################################################
# def print_user_name(*args): #인자로 들어온 사람의 이름을 출력 변수에 *가 들어가면 변수가 여러게 들어간다는 의미
# #args는 tuple로 받아요!
#     for name in args:
#         print(name,end=",")
#
# print_user_name("홍길동","심사임당")
# print_user_name("홍길동","심사임당","유관순")
################################################################################
# def print_user_name(**kwargs): # **가 들어가면 변수가 여러게 들어간다는 의미
# #kwargs는 dict로 받아요!
#     for key in kwargs.keys():
#         print(kwargs.get(key))
#     print("")
# #{"name" : "홍길동", "name2": "바보"} 이게 원래 dict
# print_user_name(name1="홍길동",name2="심사임당")
# print_user_name(name1="홍길동",name2="심사임당",name3="유관순")
########################################################################################
#decorator에 대해서 한가지 더 알아보아요!

# def my_outer(func):
#     def my_inner(*args,**kwargs):
#
#         print("decorator!! 시작")
#         func(*args,**kwargs)
#         print("decorator!! 끝")
#     return my_inner
#
# @my_outer
# def my_func():
#     print("이것은 소리없는 아우성!!")
#
# my_func()
#
# @my_outer
# def my_add(x,y):
#     print(f"두 수의 합은 = {x+y}")
#
# my_add(10,20)
############################################################################################
