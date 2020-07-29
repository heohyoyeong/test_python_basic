def calcsum(n):
    total =0

    for i in range(n+1):
        total +=i

    return total


# print("~4 =",  calcsum(4))
# print("~10 =",  calcsum(10))

def calcrange(begin, end):
    total=0
    for num in range(begin, end+1):
        total += num
    return total

# print("3~7 =", calcrange(3,7))

def printsum(n):
    total=0
    for num in range(n+1):
        total +=num
    print("~",n,"=",total)

printsum(4)
a=printsum(4)
print(a) #return 값이 없어서 출력이 없다.
b=calcrange(3,7)
print(b)
