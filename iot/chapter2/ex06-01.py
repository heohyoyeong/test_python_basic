# num =1
# total1= 0
# total2= 0
#
# while num<= 100:
#     if num%2 == 0 :
#         total1 +=num
#     else:
#         total2 +=num
#     num+=1
#
# print( total1, total2)
#
# total =0
# for num in range (2, 101, 2):
#     total += num
# print( "total = ", total)
#
# score=[92,86,68,120,56]
#
# for s in score:
#     if(s<0) or (s>100):
#         print(s)
#     else:
#         print("{}는 범위가 아닙니다.!".format(s) )
#
#
# for a in range(1,10):
#     print("{}단 시작!".format(a))
#     for b in range(1,10):
#         print("{} x {}= {}".format(a,b,a*b))
#


# print("3 +4 = ?")
#
# b=False
# for a in range(3):
#     a= int(input("정답은?:"))
#     if a==7:
#         b=True
#         break
#
#
# if b==True:
#     print("정답!")
# else:
#     print("틀렸다 이눔아!")

for a in range(10,0, -1):
    for b in range(a):
        print("*", end="")
    print()