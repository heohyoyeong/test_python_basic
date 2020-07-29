# python에서 module은 함수나 변수 또는 클래스를 모아놓은 파일을 지침
# 다른 python파일에서 불러와서 사용할 수 있다.

# module을 사용하는 이유는 코드의 재사용성과 관리목적
# python 모듈은 크게 2가지가 있다.
# 1. c언어로 구성된 binary module
# 2. python 언어로 구현된 일반 module

# module을 사용하기 위해서 사용하는 keyword : "import"
# module도 python입장에서는 객체로 관리된다.
import sys
print(sys.path) #list

sys.path.append("c:/python_data") # module을 저장할 폴더를 지정

print(sys.path)

# module을 하나 만든다(python file을 하나 생성 = module1.py 파일 생성후 c:/python_data에 저장

# import module1
#
# print(module1.my_pi)
# print(module1.my_add(10,20))
#
# import module1 as m1
#
# print(m1.my_pi)
# print(m1.my_add(10,20))
#########################################################################
# from module1 import my_add
# print(my_add(10,20))
# from module1 import * # module1에 있는 모든것을 다가져온다!
# print(my_add(10,20))
#########################################################################
# c:/python_data 안에 module1.py를 저장해 놨어요!
# c:/python_data/test_module에 module1.py를 옮김

import test_module.module1 as my_module

print(my_module.my_pi)