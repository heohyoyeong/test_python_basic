# magic function

# 1.method 이름 앞뒤에 더블 언더바(__)가있는 method
# 대표적으로 magic function =>__init__ (생성자)
# 2. class안에 정의되어 있는 특수한 형태의 method
# 3. 특수한 상황에서 그에 맞는  magic funcitondmf 호출

# class Student(object):
#     def __init__(self,name,dept): #생성자, constructor, initializer
#         self.name=name
#         self.dept=dept
#         print(f"{self.dept}학과 {self.name}학생이 생성되었습니다.")
#
#     def __del__(self):
#         print("소멸자가 호출되었습니다.")
#
# S1= Student("홍길동","기계공") #객체를 메모리에서 삭제해요!! __del__호출된다.
#
# del S1
####################################################################

# a= 100
#
# print(type(100)) #class int가 존재한다.
#
# class MyInt(int):
#     pass
#
# my_num=MyInt(100)
#
# print(my_num+ 200)
# print(my_num.__add__(200))
###########################################################
# class Student(object):
#     def __init__(self,name,dept): #생성자, constructor, initializer
#         self.name=name
#         self.dept=dept
#         print(f"{self.dept}과 {self.name}학생이 생성되었습니다.")
#
#     def __repr__(self): #overriding
#         return self.name
#
#
# stu1= Student("홍길동","기계공학")
#
# print(stu1)  #instance의 class정보와 저장되어 있는 메모리 주소가 출력
##################################################################
#
# class Car(object):
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#
#     def __lt__(self, other): #2번쨰 있는 함수가 other
#         if self.price < other.price:
#             return f"{self.model}의 가격이 더 낮습니다."
#         else:
#             return f"{other.model}의 가격의 더 낮습니다."
#
# car1= Car("G70",5000)
# car2= Car("Sonata",3000)
#
# print(car1 <car2) #__lt__ (less than)
######################################################################################################

