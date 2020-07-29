def main():
    s= "독도는 일본땅. 대마도도 일본땅"
    print(s)
    print(s.replace("일본","한국"))
    print(s)

def main2():
    message="안녕하세요"
    print(message.center(30))
    print(message.ljust(30))
    print(message.rjust(30))

def main3():
    trabler = """
    강나루 거너서
    밀밭 길을
    구름에 달 가듯이
    가는 나그네
    """
    poet= trabler.splitlines()
    for line in poet:
        print(line.center(30))

def main4():
    price= 500
    print("궁금하면" + str(price)+ "원!")

    mon=8
    day=15
    anni="광복절"
    print("%d월 %d일은 %s이다."%(mon,day,anni))

def main5():
    value=123
    print("###%d###"%value)
    print("###%5d###" % value)
    print("###%10d###" % value)
    print("###%-10d###" % value)
    print("###%1d###" % value)

def main6():
    price= [30,13500,2000]
    for p in price:
        print("가격 : %d원"%p)
    print
    for p in price:
        print("가격 : %7d원"%p)
    print
    for p in price:
        print("가격 : %-7d원"%p)
    print

def main7():
    f=123.1234567
    print("%10f" % f)
    print("%10.8f" % f)
    print("%10.5f" % f)
    print("%10.2f" % f)
    print("%.2f" % 123.126)

def main8():
    name= "한결"
    age=16
    height= 178.8
    print("이름:{}, 나이: {}, 키: {}".format(name,age,height))
    print("이름:{:s}, 나이: {:d}, 키: {:f}".format(name, age, height))
    print("이름:{:4s}, 나이: {:3d}, 키: {:.2f}".format(name, age, height))

def main9():
    name = "한결"
    age = 16
    height = 162.5
    print("이름:{0}, 나이: {1}, 키: {2}".format(name, age, height))
    print("이름:{2}, 나이: {1}, 키: {0}".format(height, age, name))
    print("이름:{name}, 나이: {age}, 키: {height}".format(age=20, height=160.9,name="길동"))


def main10():
    name="한결"
    age= 16
    height= 162.5
    print(f"이름: {name}, 나이:{age}, 키:{height:.2f}")


# main()
# main2()
# main3()
# main4()
# main5()
# main6()
# main7()
# main8()
# main9()
# main10()