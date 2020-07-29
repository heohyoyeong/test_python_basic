# def findmin(*ints):
#     b=[]
#     for a in ints:
#         b+=str(a)
#     return (b)
#
# min=findmin(2,3,4,5,6,-7)
#
# print(min)

#
# def findmin(*ints):
#     b=999999999999
#     for a in ints:
#         if b>=a:
#             b=a
#         else:
#             pass
#     return(b)
#
#
# min=findmin(2,3,4,5,1,6,-8,7)
#
# print(min)

# def swap(x,y):
#     temp= y
#     y=x
#     x=temp
#
#     print("x",x)
#     print("y",y)
#
# x=20
# y=10
#
# swap(20,10)
def rand(start,end):
    import random
    rng=end-start+1
    return int(random.random() * rng) + start

def main():
    """1~6까지의 정수를 임의로 출력해주는 함수"""
    start =1
    end =100
    number =rand(start,end)

    for a in range(1, 6):
        x = int(input(str(a)+"번쨰 추측값:"))
        if number<x:
            print(x,"보다 작습니다.")
        elif number>x:
            print(x,"보다 큽니다.")
        else:
            return print("정답입니다.")
    print("실패했습니다. 정답은", number,"입니다.")

main()




