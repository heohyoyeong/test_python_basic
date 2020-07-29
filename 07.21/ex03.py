# exception (예외)
# compile time error (코드를 작성하는 중에 나오는 에러 (문법오류) : 실행자체가 안됨)
# runtime error (실행시 발생하는 오류)

# 어떤 runtime error들은 비정상 종료되지 않고 프로그램을 지속적으로 수행시킬수있는 방법이 존재
# 에러 중에 극복이 가능한 에러를 exception 이라한다.
###############################################################################################
# exception 처리는 하나의 구문밖에 없다.
# try~
# except
# else
# finally

def my_func(my_list):
    total_sum=0

    try: #exception 처리를 하기위하여 무조건 있어야함
        total_sum = my_list[0] + my_list[1] +my_list[2]
        print("try가 수행되었어요")
    except Exception: #Exception은 발생할 수 있는 모든 오류를 지칭함
        print("오류가 존재합니다.") #예외 처리를 해야함.
    else:
        print("오류가 없습니다.") #오류가 없을 경우 try다음으로 진행

    finally: #무조건 수행됨
        print("무조건 수행되요!")

    return 3

# my_func([1,2,3]) #오류 미발생
# my_func([1,2]) #오류 발생

print(my_func([1,2]))

# def nigg(my_list):
#     total_sum=0
#     for tmp in my_list:
#         total_sum+=tmp
#     return total_sum
#
# print(nigg([1,2,3]))