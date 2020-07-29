# 1990년도 이전
# 가장 대표적인 프로그램 작성 방식으로
# 구조적 프로그래밍(절차적 프로그래밍)
# 프로그램 작성시 기능으로 세분화해서 각각의 기능을 모듈로 제작 프로그램을 작성

# 세상이 변하고 프로그램의 유지보수가 중요하게 대두되었어요!!

# 현실세계의 해결해야 하는 문제에 대한 구성요소를 파악
# => 은행지점, 고객, 텔러,  ATM, 계좌 => 개체(object)
# => Object Oriented Programming (OOP)
# => 개체들을 파악해서 그 개체들간의 관계를 프로그래밍 하는 방식을
# => 객체지향 프로그래밍이라고 해요!!

# => 개체들을 파악한 후 이 각각의 개체를 프로그램적으로 묘사해야 해요
# => 객체 모델링

# 예) 사람을 프로그램적으로 묘사해보아요(객체모델링을 해 보아요!)
# 추상화(Abstraction)과정을 거쳐서 사람을 객체모델링 할 꺼예요!
# 이런 개체들은 속성, 행위가 있드라!!
#             변수(property, member field, field),
#             함수(method)
# class라는걸 이용해서 추상화과정을 거친 개체를 프로그램적으로 표현하게되요!
# class => 1. 객체모델링의 수단.

# class 사람
#       키(변수) height => float
#       몸무게(변수) weight => float
#       나이(변수) age => int
#       이름(변수) name => str
#       걷는다(메소드)
#       말한다(메소드)
#       잔다(메소드)

# class는 data type의 관점에서 봤을때는 기존 데이터타입을 이용해서
# 새로운 data type을 만드는 것이라고 볼 수 있어요!
# class => 추상적인 데이터 타입이라고 불러요!( Abstract data type )
#       => ADT

#########################################################

# 구조적 프로그래밍(절차적 프로그래밍)
# 프로그램 작성 시 기능으로 세분화해서 각각의 기능을 모듈화(함수화)해서 구현
# 프로그램 구조를 이해하기 쉽고 프로그램을 빠르게 만들 수 있어요!
# 프로그램 규모가 커지만 유지보수와 코드의 재사용에 한계가 오게되요!

# 객체지향 프로그래밍
# 현실세계의 해결해야 하는 문제를 그대로 프로그램으로 묘사(표현)
# 프로그램을 구성하는 주체들(개체,객체,Object)을 파악하고
# 그 객체들간의 데이터 흐름에 초점을 맞추어서 프로그램을 작성
# 프로그램을 설계하고 작성이 상대적으로 어려워요!
# 일단 제대로 작성된 객체지향 프로그램은 유지보수와 재사용성에 상당한 이점.

############################################################

# 학생의 이름, 학과, 학번, 평균평점을 저장하는 방법

# stu_name = "홍길동"
# stu_dept = "심리학과"
# stu_num = "20201134"
# stu_grade = 3.5

# 만약 3명의 학생이 있으면 어떻게 하나요??

# stu1_name = "홍길동"
# stu1_dept = "심리학과"
# stu1_num = "20201134"
# stu1_grade = 3.5
#
# stu2_name = "김길동"
# stu2_dept = "컴퓨터"
# stu2_num = "20201135"
# stu2_grade = 2.0
#
# stu3_name = "신사임당"
# stu3_dept = "경영학과"
# stu3_num = "20201138"
# stu3_grade = 4.0

# 코드가 너무 불필요하게 반복적이고 확장성이 없는 코드가 됬어요 ㅡㅜ

# stu_name = ["홍길동", "김길동", "신사임당"]
# stu_dept = ["심리학과", "컴퓨터", "경영학과"]
# stu_num = ["20201134","20201135","20201138"]
# stu_grade = [3.5, 2.0, 4.0]

# index를 이용해 처리하는게 쉬운작업은 아니고 코드에 모든 의미가 다
# 내포되어 있는게 아닌 문제가 발생.

# 어떻게 하면 이런내용을 class 이용해서 객체지향적으로 표현할 수 있을까??
# 학생이라는 개념을 프로그램적으로 모델링을 해 보아요!

# class Student(object):
#     def __init__(self,name,dept,num,grade):
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
# students =[]
# students.append(Student("홍길동","심리학과","20201134",3.5))
# students.append(Student("김길동","컴퓨터","20201135",2.0))
# students.append(Student("신사임당","경영학과","20201138",4.0))

#######################################################

## Python은 객체지향 언어예요!!
## Python에서 나오는 모든것은 다 객체(instance)예요

# my_list = [10]
# print(type(my_list))   # <class 'list'>

# class list(object):
#       ~~~
#       ~~~
#       ~~~

# 숫자도 객체(instance)고, 리스트도 객체(instance)고
# str(문자열)도 객체고, 함수도 객체예요!!

# 객체(instance)가 있단는건 => class가 존재한다는얘기예요!!
# 객체(instance) => 변수,method

# 객체(instance)란 속성과 같은 여러가지 데이터 + 메소드를 가지고있는
# 데이터 구조를 지칭해요!

# class Student(object):
#     def __init__(self,name,dept,num,grade):   # constructor(생성자)
#         self.name = name                      # initializer
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):
#         return self.name
#
#     def change_dept(self,tmp_dept):
#         # tmp_dept가 정상적인 학과인지 check하는 코드
#         self.dept = tmp_dept
#
#
# student = Student("홍길동", "심리학과", "20201133", 4.5)
#
# # information hiding(정보은닉) 개념도 알아둬야 해요!!
# student.change_dept("임상병리학과")
# #student.dept = "임상병리학과"
#
# print(student.dept)

####################################################

# python이 제공하는 내장함수 중 dir() 에 대해서 알아보아요!!
# 객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알려줘요!

# class Student(object):
#     def __init__(self,name,dept,num,grade):   # constructor(생성자)
#         self.name = name                      # initializer
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):
#         return self.name
#
#     def change_dept(self,tmp_dept):
#         self.dept = tmp_dept
#
# student = Student("홍길동", "심리학과", "20201133", 4.5)
# print(dir(student))

# 한가지를 더 생각해보아요!!
# student.depts = "철학과"
# print(dir(student))
# ['__class__', '__delattr__', '__dict__',
#  '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__le__', '__lt__',
#  '__module__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', '__weakref__',
#  'change_dept', 'dept', 'grade', 'name', 'num']

## python의 함수도 객체예요!!
# def my_func(a,b):
#     return a+b
#
# print(dir(my_func))
#
# my_func.myName = "홍길동"
# print(dir(my_func))

# class Student(object):
#
#     scholarship_rate = 3.0    # class variable
#
#     def __init__(self, name, dept, num, grade):   # constructor(생성자)
#         self.name = name                      # initializer
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def is_scholarship(self):
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
#
# student = Student("홍길동", "심리학과", "20201133", 2.0)
# print(student.is_scholarship())

#######################################################

# class Student(object):
#
#     scholarship_rate = 3.0   # class variable
#
#     def __init__(self,name,dept,num,grade):   # constructor(생성자)
#         self.name = name                      # initializer
#         self.dept = dept                      # instance variable을
#         self.num = num                        # 선언하고 초기화
#         self.grade = grade
#
#     def __repr__(self):
#         return self.name
#
#     def is_scholarship(self):                # instance method
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
# student = Student("홍길동","심리학과","20203311",4.0)
# print(student.is_scholarship())
#
# student.scholarship_rate = 4.5
# print(student.is_scholarship())

##########################################################

# namespace(네임스페이스)
# 객체가 가지는 데이터를 나누어서 관리하는 공간
# instance namespace
# class namespace
# superclass namespace
# intance namespace < class namespace < superclass namespace

# python은 동적으로 속성이나 method를 추가할 수 있어요!

# print(student.dept)
# student.depts = "컴퓨터"   # depts 속성이 추가되요!!
#
# print(student.depts)

# class Student(object):
#
#     scholarship_rate = 3.0   # class variable
#
#     def __init__(self,name,dept,num,grade):   # constructor(생성자)
#         self.name = name                      # initializer
#         self.dept = dept                      # instance variable을
#         self.num = num                        # 선언하고 초기화
#         self.grade = grade
#
#     @classmethod   # class method decorator
#     def change_scholaraship(cls,rate):
#         cls.scholarship_rate = rate
#         print("장학금 기준이 변경되었어요!")
#
#     @staticmethod
#     def is_valid_schlarship(rate):
#         if rate < 0:
#             print("장학금 기준 학점은 음수가 될 수 없습니다.")
#
#
#     def is_scholarship(self):                # instance method
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
# student = Student("홍길동","심리학과","20203311",4.0)
#
# student.dept = "컴퓨터"
#
# change_rate = -3.0
# Student.is_valid_schlarship(change_rate)
# Student.change_scholaraship(change_rate)


# instance method(self인자를 가지고 있는 method)는 하나의
# 인스턴스에 한정된 데이터를 생성,변경,참조하기 위해서 사용되요!

# class method는 클래스를 인자로 받아서 class variable을
# 생성, 변경, 참조하기 위해서 사용

# static method는 class안에서 정의된 일반 함수

###########################################################

# information hiding(정보은닉)
# instance가 가지는 속성은 매우 매우 중요한 데이터이기때문에
# 외부에서 직접적으로 access하는건 좋지 않아요!

# 어떻게 외부에서 직접적으로 access하는 것을 막을 수 있는가?
# 프로그래밍 언어마다 달라요!!
# Java => access modifier(접근제어자)
#         public vs. private

# Python에서 속성에 직접적으로 접근하는 것을 막기위해서는 어떻게
# 해야 하나요?? => private으로 지정하려면 어떻게 해야 하나요?
# "__"

# class Student(object):
#
#     def __init__(self,name,dept,num,grade):   # constructor(생성자)
#         self.name = name                      # initializer
#         self.__dept = dept                      # instance variable을
#         self.num = num                        # 선언하고 초기화
#         self.grade = grade
    # private으로 처리된 속성이 있으면 외부에서 직접적인
    # access가 안되기 때문에 method를 이용해서 사용하도록 처리
    # private으로 되어 있는 속성의 값을 알아오는 용도의 method가 필요
    # ==> getter (getter의 이름을 짓는 방법이 정해져 있어요!!)
    # def get_dept(self):
    #     return self.__dept
    # ==> setter는 값을 설정해주는 method
#     def set_dept(self,dept):
#         self.__dept = dept
#
#     def __print_date(self):
#         return self.name
#
# student = Student("홍길동","심리학과","20203311",4.0)
# print(student.get_dept())
# student.set_dept("컴퓨터")
# print(student.get_dept())

# 여기까지가 단일 class에 대한 이론적인 내용이예요!!
########################################################

# 객체지향을 하는 이유는 => 유지보수와 재사용성
# 재사용성을 위한 대표적인 객체지향 기법 => Inheritance(상속)

# 두 개의 class를 이용해서 우리 상속을 알아보아요!!
# Unit class, Marine class
# Unit class => 모든 unit이 공통으로 가지고 있는 속성과 method로 구성
#               super class로 사용, base class
# Marine => sub class

# class object:
#       ~
#       ~
# python의 모든 class는 object class예요!!
# python의 모든 class는 object class를 상속해야 해요!

# class Unit(object):
#
#     def __init__(self,damage,life):
#         self.utype = self.__class__.__name__
#         self.damage = damage
#         self.life = life
#
#     def show_status(self):
#         print("직업 : {}".format(self.utype))
#         print("공격력 : {}".format(self.damage))
#         print("생명력 : {}".format(self.life))
#
#
# class Marine(Unit):
#
#     def __init__(self,damage,life,range_upgrade):
#         super(Marine, self).__init__(damage,life)
#         self.range_upgrade = range_upgrade
#
#     def show_status(self):
#         super(Marine, self).show_status()
#         print("사거리 업그레이드 유무 : {}".format(self.range_upgrade))
#
# marine_1 = Marine("100","100",True)
#
# marine_1.show_status()

#################################################

# 사용할 유닛들은 Marine, Medic, Vulture, Dropship 4종류의 unit

# super class
# class Unit(object):
#
#     def __init__(self,damage,life):
#         self.utype = self.__class__.__name__
#         self.damage = damage
#         self.life = life
#
#     def show_status(self):
#         print("직업 : {}".format(self.utype))
#         print("공격력 : {}".format(self.damage))
#         print("생명력 : {}".format(self.life))
#
#     def attack(self):
#         pass
#
#
# class Marine(Unit):
#
#     def __init__(self,damage,life,range_upgrade):
#         super(Marine, self).__init__(damage,life)
#         self.range_upgrade = range_upgrade
#
#     # overriding
#     def show_status(self):
#         super(Marine, self).show_status()
#         print("사거리 업그레이드 유무 : {}".format(self.range_upgrade))
#
#     # overriding
#     def attack(self):
#         print("마린이 총으로 공격합니다. 땅땅!!!")
#
#     def stimpack(self):
#         if int(self.life) < 20:
#             print("체력이 낮아서 스팀팩 수행이 불가능합니다.")
#         else:
#             # self.life -= 10
#             # self.damage *= 1.5
#             print("마린이 스팀팩을 사용했어요!!")
#
# class Medic(Unit):
#
#     # overriding
#     def attack(self):
#        print("메딕이 치료합니다. 힐힐!!!")
#
#
# class Vulture(Unit):
#
#     def __init__(self,damage,life,amount_of_mine):
#         super(Vulture, self).__init__(damage,life)
#         self.amount_of_mine = amount_of_mine
#
#     # overriding
#     def attack(self):
#         print("벌쳐가 공격합니다. ~~~")
#
# class Dropship(Unit):
#
#     # overriding
#     def attack(self):
#         print("특정 목표지점으로 이동합니다. 쓩!!")
#
#     def board(self,unit_list):
#         self.unit_list = unit_list
#         print("유닛들을 드랍쉽에 태워요!!")
#
#     def drop(self):
#         print("모든 unit이 드랍쉽에서 내립니다.")
#         return self.unit_list
#
# # marine을 생성합니다. 3마리
#
# marine_1 = Marine("100","100",False)
# marine_2 = Marine("100","100",False)
# marine_3 = Marine("100","100",False)
#
# # medic을 생성합니다. 1마리
# medic = Medic("0","100")
#
# # vulture를 생성합니다. 2마리
# vulture_1 = Vulture("200","100",3)
# vulture_2 = Vulture("200","100",3)
#
# # list를 이용해서 여러개의 객체를 저장할꺼예요!
# troop = list()
# troop.append(marine_1)
# troop.append(marine_2)
# troop.append(marine_3)
# troop.append(medic)
# troop.append(vulture_1)
# troop.append(vulture_2)
#
# # Dropship 생성
# dropship = Dropship("0","100")
#
# # dropship에 유닛들을 태워요!!
# dropship.board(troop)
#
# # 공격지점으로 이동
# dropship.attack()
#
# # 공격지점에서 내리기
# my_list = dropship.drop()
#
# # 스팀팩을 쓰고 공격하기
# for unit in my_list:
#     if isinstance(unit,Marine):
#         unit.stimpack()
#     unit.attack()

####################################################
# 공유폴더에 들어가시면 student_score.txt라는 파일이 있어요!
# 각 사람에 대한 데이터를 읽어서
# 성적순으로 출력하시면 되요! 출력양식은 다음과 같습니다.
# 1등 아이유 95.6
# 2등 홍길동 89.3
# 3등 최길동 88.2

class Student(object):

    def __init__(self, name, kor, eng, math):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.avg = round((kor + eng + math) / 3, 1)

    def __repr__(self):
        return "{} {}".format(self.__name, self.avg)


file = open("C:/python_data/student_score.txt","r")
stu_list = list()

while True:
    line = file.readline()
    if not line:
        break
    stu_data = line.split(",")
    stu_list.append(Student(stu_data[0],int(stu_data[1]),
                            int(stu_data[2]),int(stu_data[3])))

file.close()

result = reversed(sorted(stu_list, key=lambda student: student.avg))

idx = 1
for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1

###############################






