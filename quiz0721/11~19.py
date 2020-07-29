#######################################################################################
## 문제 11.
## 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

## n → n / 2 (n이 짝수일 때)
## n → 3 * n + 1 (n이 홀수일 때)

## 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도
## 마지막에는 1로 끝나리라 생각됩니다.
## (이런 수들을 우박수 hailstone sequence라 합니다.)

## 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데
## 가장 긴 과정을 거치는 숫자는 얼마입니까?
## 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.
#######################################################################################
def golow(x):
    if x%2==0:
        a=x/2
        return a
    if x%2==1:
        b=x*3+1
        return b

k=1000000
a=0

while True:
    b=golow(k)
    k=b
    a+=1
    if b==1:
        break
print(a)
#######################################################################################
## 문제 12.
## 다음과 같은 특성을 갖는 숫자의 개수를 찾는 기능을 구현합니다.
## 입력으로 두개의 숫자( x, y )를 이용합니다.
## - 두 개의 숫자 x와 y를 이용하여,
##   x초과 y미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##   되는 숫자를 찾습니다.
## - 숫자들을 모두 찾은 후 해당 숫자가 총 몇 개인지를 출력합니다.

## 예1) 두 개의 숫자 1과 100이 주어졌을 경우,
##      1초과 100미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      - 20의 경우 각 자리 숫자를 모두 더한 값이 2이므로, 적합하지 않다.
##      - 23의 경우 각 자리 숫자를 모두 더한 값이 5이므로, 적합하다.
##      [총 개수] 19

## 예2) 두 개의 숫자 5와 500이 주어졌을 경우,
##      5초과 500미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      [총 개수] 98

## 입력으로 주어지는 두 개의 수 : 100 10000
#######################################################################################
# def try12(x,y):
#     b=list()
#     k=list()
#     for a in range(x,y):
#         str(a)
#         b.append(a)
#         c=b[0]
#         c=int(c)
#         d=b[1]
#         d=int(d)
#         e=b[2]
#         e=int(e)
#         f=c+d+e
#         if f%5==0:
#             k.append(a)
#     print(k)

def try12(x,y):
    b=list()
    k=list()
    for a in range(x,y):
        b = f"{a}"
        c=b[0]
        c=int(c)
        d=b[1]
        d=int(d)
        e=b[2]
        e=int(e)
        f=c+d+e
        if f%5==0:
            k.append(a)
    return print(len(k))

try12(100,10000)
#######################################################################################
## 문제 13.
## 6자리 이상 9자리 미만의 수를 입력으로 사용합니다.

## 수의 중앙을 기준으로 두 개의 수로 분리한 후 큰 수를 선택한다.
## - 수의 숫자개수가 홀수 개인 경우 수의 중앙 숫자를 기준으로
##   왼쪽과 오른쪽 수로 분리
## - 수의 숫자개수가 짝수 개인 경우 수를 반으로 나누어
##   왼쪽과 오른쪽 수로 분리
## 예1) 1234567 -> (123, 567) -> (567)
## 예2) 34217869 -> (3421, 7869) ->(7869)

## 입력으로 제공된 수를 더 이상 두 개의 수로 분리할 수 없을 때까지
## 과정을 반복하여 남은 최종 숫자를 구해 출력한다.
## 예1) 567 -> (5, 7) -> (7)
## 예2) 7869 -> (78, 69) -> (78) -> (7, 8) -> (8)
#######################################################################################

def try13(x):
    b = f"{x}"
    c = len(b)
    d = list()
    for a in range(0, c):
        d.append(b[a])

    while True:
        c = len(d)
        if c%2==0:
            t=int(len(d)/2)
            for k in range(0,t):
                d.pop(0)
        if c%2 == 1:
            t =int(len(d)/2+1)
            for k in range(0, t):
                d.pop(0)
        if len(d)==1:
            return print(d)
try13(34217869)
#######################################################################################
## 문제 14.
## 2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

## 2**1000의 각 자리수를 모두 더하면 얼마입니까?
#######################################################################################
def try14(x):
    b = f"{x}"
    c = len(b)
    d = list()
    f=0
    for a in range(0, c):
        d.append(b[a])
        f+=int(b[a])
    print(f)
try14(2**1000)
#######################################################################################
## 문제 15.
## 각 부품의 생산정보가 문자열로 제공된다.
## [부품생산정보] : A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8

## 각 부품정보는 부품명과 품질데이터로 구성된다.
## - A,B,C 3개의 부품이 있으며 품질은 1이상 10미만의 정수.
##   예) A7 : A부품, 품질 7

## 생산정보에서 품질이 7이상인 부품만을 순서대로 선택한다.
## [생산정보] A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8
## [품질이 7이상인 부품 목록] A7A8B9A8B9C7C7B9A7B8C9A8

## 품질이 7이상인 부품들을 조립해 완성품을 만든다.
## A, B, C 세 부품이 순서대로 있을 때만 부품을 조립한다.
## A7A8B9A8B9C7C7B9A7B8C9A8 => A8B9C7, A7B8C9 2개 조립
## 조립한 부품의 목록과 전체 조립한 개수를 출력
#######################################################################################
# def try15():
#     a = input("입력하세요:")
#     b=str(a)
#     c=len(b)
#     d=list()
#     t1=list()
#     a1=list()
#     b1=list()
#     c1=list()
#
#     for z in range(0, c):
#         d.append(b[z])
#     print(type(d))
#     e=int(c/2)
#     for z in range(0,e,2):
#         if d[z]=='A':
#             if int(d[z+1]) >6:
#                 a1.append(d[z])
#                 a1.append(d[z+1])
#         elif d[z]=='B':
#             if int(d[z + 1]) > 6:
#                 b1.append(d[z])
#                 b1.append(d[z + 1])
#         elif d[z]=='C':
#             if int(d[z + 1]) > 6:
#                 c1.append(d[z])
#                 c1.append(d[z + 1])
#
#
#     print(a1)
#     print(b1)
#     print(c1)

def try15():
    a = input("입력하세요:")
    b=str(a)
    c=len(b)
    d=list()
    t1=list()
    t2=list()


    for z in range(0, c):
        d.append(b[z])
    e=int(c/2)
    for z in range(0,c,2):
        if d[z]=='A':
            if int(d[z+1]) >6:
                t1.append(d[z])
                t1.append(d[z+1])
        elif d[z]=='B':
            if int(d[z + 1]) > 6:
                t1.append(d[z])
                t1.append(d[z + 1])
        elif d[z]=='C':
            if int(d[z + 1]) > 6:
                t1.append(d[z])
                t1.append(d[z + 1])
    t=len(t1)
    for zz in range(0,t-2):
        if t1[zz]=='A':
            if t1[zz+2]=='B':
                if t1[zz+4]=='C':
                    t2.append(t1[zz])
                    t2.append(t1[zz+1])
                    t2.append(t1[zz+2])
                    t2.append(t1[zz+3])
                    t2.append(t1[zz+4])
                    t2.append(t1[zz+5])

    print(t2)



try15()




#######################################################################################
## 문제 16.
## n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.

## 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
## 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.

## 100! 의 자리수를 모두 더하면 얼마입니까?
#######################################################################################
def try16(x):
    b=1
    for a in range(1,x+1):
        b=b*a

    b = f"{b}"
    c = len(b)
    d = list()
    f = 0
    for a in range(0, c):
        d.append(b[a])
        f += int(b[a])
    print(f)
# try16(100)
#######################################################################################
## 문제 17.
## 최소 10개 이상 최대 20개 이하의 숫자로 구성된 숫자목록이 배열 혹은 리스트 형태로 제공된다.
## 숫자목록 : 1,3,4,5,7,9,2,3,4,7

## 아래의 순서로 숫자목록의 숫자를 교환하여 재배치한다.
## 1) 숫자목록의 앞에서부터 4개의 숫자를 선택한다.
##    목록에서 숫자 선택 : [1,3,4,5],7,9,2,3,4,7
## 2) 선택된 4개의 숫자의 합을 구한다.
##    4개의 숫자 합 : [1,3,4,5],7,9,2,3,4,7 => 13
## 3) 첫 번째와 두 번째 숫자를 교환하고 세 번째와 네 번째 숫자를 교환한다.
##    숫자 교환 : [3,1,5,4],7,9,2,3,4,7
## 4) 오른쪽으로 한칸씩 이동하여 순서대로 1,2,3번 과정을 반복해 숫자목록의 숫자를 재배치한다.
## 예) [1,3,4,5],7,9,2,3,4,7 =>
##     [3,1,5,4],7,9,2,3,4,7 =>
##     3,[1,5,4,7],9,2,3,4,7 -> …

## 맨 마지막까지 도달했을 때 선택된 4개의 숫자의 합이 가장 큰 값과 그 때의 숫자목록을 출력

## [초기 입력 데이터]
## 1 3 4 5 7 9 2 3 4 7
## ---------------------------------------------------------------
## [5번째 선택되는 4개의 숫자]: 2 1 3 4
## ---------------------------------------------------------------
## [선택된 4개의 수의 최대 합]: 21


## [초기 입력 데이터]
## 10 15 3 5 9 5 7 8 9 15 44 54 15 67 32 25 48 98 44 56
## ---------------------------------------------------------------
## [7번째 선택되는 4개의 숫자]: 9 10 15 3
## ---------------------------------------------------------------
## [선택된 4개의 수의 최대 합]: 159
## ---------------------------------------------------------------
#######################################################################################
def try17(*arg):
    a = list(arg)
    b = len(a)
    d = list()
    e = list()
    c = b - 3
    f = 0
    for g in range(0, c):
        i = a[g]
        ii = a[g + 1]
        a[g] = ii
        a[g + 1] = i
        iii = a[g + 2]
        iiii = a[g + 3]
        a[g + 2] = iiii
        a[g + 3] = iii
        for h in range(g, g+4):
            d.append(a[h])
        for k in range(0, 4):
            f += int(d[k])
        d=list()
        e.append(f)
        f = 0
    print(max(e))
# try17(1,3,4,5,6,7,9,2,3,4,7)
#######################################################################################
## 문제 18.
## 어떤 대상을 순서에 따라 배열한 것을 순열이라고 합니다.
## 예를 들어 3124는 숫자 1, 2, 3, 4로 만들 수 있는 순열 중 하나입니다.

## 이렇게 만들 수 있는 모든 순열을 숫자나 문자 순으로 늘어놓은 것을
## 사전식(lexicographic) 순서라고 합니다.

## 0, 1, 2로 만들 수 있는 사전식 순열은 다음과 같습니다.
## 012   021   102   120   201   210


## 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서
## 1,000,000번째는 무엇입니까?

#######################################################################################



# def try18(*arg):
#     a = list(arg)
#     b = len(a)
#     c=list()
#     d=list()
#     e = 1
#
#     for a in range(1, b-1):
#         e = e * a # e n-1!값
#
#     for z in range(0,b):
#         y=str(a[z])
#         c.append(y) #문자열로 1번에 저장 기본
#
#         for zz in range(0,e):
#             while True:
#                 asdfasdf
#             p=akdfajsdf
#             c.append(p)
###################################
# a=[1,2,5,4,7,4,2,5,5,4]
# b = len(a)
# d=list()
#
# for z in range(0, b):
#     c=str(a[z])
#     d.append(c)
# for zz in range(0,b):
#     e=str.join('',d)
#########################################
# def try18(*arg):
#     a = list(arg)
#     b = len(a)
#     c = list()
#     d = list()
#     e = 1
#     for a in range(1, b):
#         e = e * a  # e n-1!값
#
#     while True:
#         for z in range(0,b):
#             y = str(a[z])
#             c.append(y)
#             for zz in range(0,b-1):
#######################################################################################
## 문제 19.
## 입력으로 제공되는 숫자열에서 짝수와 홀수를 추출하여 새로운 숫자열을 생성한다.
## 1) 입력된 숫자열에서 짝수와 홀수를 순서대로 추출한다.
##    [입력] 78235169
##    [짝수 추출] 826
##    [홀수 추출] 73519
## 2) 추출된 짝수의 뒤에 추출된 홀수를 연결하여 새로운 숫자열을 생성한다.
##    [짝수와 홀수 연결] 82673519 #ㅇㅋ!

## 결과숫자열을 앞에서부터 순서대로 뺄셈 연산 또는 덧셈 연산 한다.
## 숫자열의 앞에서 부터 순서대로 뺄셈 연산한다.
## 단, 앞선 연산 결과가 0 이하이면 그 차례에는 덧셈 연산한다.
## [결과 숫자열] 82673519
## [각 수의 연산 순서와 방법]
##   8 - 2 = 6
##   6 – 6 = 0
##   0 + 7 = 7 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   7 – 3 = 4
##   4 – 5 = -1
##  -1 + 1 = 0 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   0 + 9 = 9 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
## [연산 결과] 9

## [입력]: 78235169
## [출력]: 9

## [입력]: 693756874
## [출력]: 7
#######################################################################################
def try19(x):
    zac = list()  # 짝수
    hol = list()  # 홀수
    newzac=list()

    b = f"{x}"
    c = len(b)
    d = list()
    for a in range(0, c):
        f = int(b[a])
        d.append(f)
    for z in range(0, c):
        if d[z] % 2 == 0: #짝수이면
            zac.append(d[z])
        if d[z] % 2 == 1: #홀수이면
            hol.append(d[z])
    newzac=zac.__add__(hol)
    pl=list()
    fl=newzac[0]-newzac[1]
    pl.append(fl)
    for z in range(0,c-2):
        if pl[z] > 0:
            zz=pl[z]-newzac[z+2]
            pl.append(zz)
        else:
            zz=pl[z]+newzac[z+2]
            pl.append(zz)

    print(pl[c-2])

# try19(693756874)