# class Student(object):
#     scolarship_rate=3.0 # class variable 모든 instance가 공유하는 변수
#
#     def __init__(self,name,dept,num,grade): #constructor or initializer
#         self.name=name
#         self.dept=dept
#         self.num=num
#         self.grade=grade               #name, dept 같은 것들이 instance variable
#
#     def __repr__(self):
#         return self.name
#
#     def is_scolarship(self):
#         if self.grade > self.scolarship_rate: #이거 질문해야겠다.
#             return True
#         else:
#             return False
#
# student= Student("용용이","의료","20201111",4.0)
# student.scolarship_rate = 4.5 # 교체되지않고 instance namespace에 추가된다.
# print(student.is_scolarship())


###########################################################

# namespace(네임스페이스)

# 객체가 가지는 데이터를 나누어서 관리하는 공간
# instance namespace
# class namespace
# superclass namespace
# instance namespace < class namespace < superclass namespace

# python은 동적으로 속성이나 method를 추가할수 있다.
# print(student.dept)
# student.depts="컴퓨터"
# print(student.depts)

class Student(object):
    scolarship_rate=3.0 # class variable 모든 instance가 공유하는 변수

    def __init__(self,name,dept,num,grade): #constructor or initializer
        self.name=name
        self.dept=dept
        self.num=num
        self.grade=grade               #name, dept 같은 것들이 instance variable


    @classmethod #class method decorator
    def change_scholarship(cls,rate):
        cls.scolarship_rate =rate
        print(f"장학금 기준이 {rate}로 변경되었습니다.")


    @staticmethod #static method decorator
    def is_valid_schlarship(rate): # static method는 class namespace안에 정의된 일반 함수 self와 cls를 넣지않는다!
        if rate <0:
            print("장학금 기준 학점은 음수가 될 수 없습니다.")


    def is_scolarship(self):
        if self.grade > self.scolarship_rate:
            return True
        else:
            return False

a1= Student("용용이","의료","20201111",3.5)

change_rate=-3.0
Student.change_scholarship(change_rate)
Student.is_valid_schlarship(change_rate)
print(a1.is_scolarship())

# instance method는 self인자를 가지고있는 method다.
# instance에 한정된 데이터를 생성,변경,창조하기 위해서 사용된다.
# class method는 class를 인자로 받아 class variable을 생성,변경,창조하기 위해서 사용된다.
# static method는 class namespace안에 정의된 일반 함수

############################################################################


# information hiding(정보은닉)
# instance가 가지는 속성은 매우 매우 중요한 데이터이기 떄문에 외부에서 직접적으로 access하는 건 좋지 않다.
# 어떻게 외부에서 직접적으로 access하는 것을 막을수있는가?
# 프로그래밍 언어마다 다르다!
# java  =>  access modifier(접근제어자)
#           public vs privates
# python에서 속성에 직접적으로 접근하는 것을 막기 위해서는 어떻게 해야하는가
# "__"를 사용한다!


class Student(object):
    def __init__(self, name, dept, num, grade):  # constructor or initializer
        self.name = name
        self.__dept = dept  # private 처리를 한것 " __ "
        self.num = num
        self.grade = grade  # name, dept 같은 것들이 instance variable

    # private로 처리된 속성이 있으면 외부에서 직접적인 access가 안되기때문에 method를 이용해서 사용하도록 처리
    # private으로 되어있는 속성의 값을 알아오는 용도의 method가 필요 => getter (getter의 이름을 짓는 방법이 정해져있음)
    # get_dept(self), get_name(self)와 같이 함수를 제작하여 클래스 내부에서 호출

    def get_dept(self):
        return self.__dept

    # setter는 값을 서정해주는 method
    def set_dept(self, dept):
        self.__dept = dept

    # private method 제작!
    def __print_data(self):
        return self.name


a1 = Student("용용이", "의료공학과", "20201111", 3.5)
# print(a1.__dept) #출력오류

print(a1.get_dept())  # 이렇게하면 된다!
a1.set_dept("기계공학과")
print(a1.get_dept())

# 여기까지가 단일 class에 대하여 이론적인 내용

##################################################################################################