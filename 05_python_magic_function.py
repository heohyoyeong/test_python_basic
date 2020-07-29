
# Magic function

# - 1. method의 이름 앞뒤에 더블 언더스코어(__)가 붙어있는
#       method를 지칭해요!
#       대표적인 magic function => __init__ (생성자)
# - 2. class안에 정의되어 있는 특수한 형태의 method
# - 3. 특수한 상황에서 그에 맞는 magic function이 호출됩니다.!!

# class Student(object):
#
#     def __init__(self,name,dept):    # 생성자, constructor, initializer
#         self.name = name
#         self.dept = dept
#         print("{} 학과 {} 학생이 생성되었습니다.".format(self.dept,
#                                              self.name))
#
#     def __del__(self):
#         print("소멸자가 호출되었어요!!")
#
# stu1 = Student("홍길동","심리")
#
# del stu1     # 객체를 메모리에서 삭제해요!! __del__ 호출되요!

#############################################

# a = 100
# print(type(a))   # class int가 존재해요!!

# class MyInt(int):
#     pass
#
# my_num = MyInt(100)
# print(my_num + 200)
# print(my_num.__add__(200))

#######################################

# class Student(object):
#
#     def __init__(self,name,dept):    # 생성자, constructor, initializer
#         self.name = name
#         self.dept = dept
#         print("{} 학과 {} 학생이 생성되었습니다.".format(self.dept,
#                                              self.name))
#     def __repr__(self):
#         return self.name
#
# stu1 = Student("홍길동","심리")
#
# print(stu1)  # instance의  class정보와 저장되어 있는 메모리 주소가 출력

#############################################

class Car(object):
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def __lt__(self, other):
        if self.price < other.price:
            return "{} 가격이 더 낮아요!!".format(self.model)
        else:
            return "{} 가격이 더 높아요!!".format(self.model)

car1 = Car("G70",5000)
car2 = Car("Sonata",3000)

print(car1 < car2)
#######################################################