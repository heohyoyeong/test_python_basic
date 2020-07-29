def calcstep(begin, end, step =1):
    total =0
    for num in range(begin, end +1, step):
        total += num
    return total

# print("1~10=", calcstep(1,10,2))
# print("1~100=", calcstep(1,100))

def intsum(*ints):
    total=0
    for num in ints:
        total += num
    return total

#print(intsum(1,2,3))
#print(intsum(8,9,6,2,9,7,5,8))

# a=8
# if a%2==0:
#     print("짝수")
# else:
#     print("홀수")


def calcsteps(**args):
    begin=args["begin"]
    end=args["end"]
    step=args["step"]
    total = 0

    for num in range(begin, end + 1, step):
        total += num
    return total

# print("3~5=", calcsteps(begin=3,end=5,step=1))

def calcscore(name,*score,**option):
    print(name)
    total=0
    for s in score:
        total +=s
    print("총점:", total)
    if(option['avg']==True):
        print("평균:", total/len(score))

# calcscore("길동홍",100,50,90,80,70,60,101,avg=True)


def kim():
    temp="김 함수"
    print(temp)

def lee():
    temp= 2**10
    return temp

def park(a):
    temp= a*2
    print(temp)

price= 1000

def sale():
    """이런건 함수를 뜯어봐라"""
    global price
    price=500


help(id)