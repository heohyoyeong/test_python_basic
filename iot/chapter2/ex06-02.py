# ROCK=0
# SCISSORS=1
# PAPER=2
w=0
r=0
d=0

import random

# com_ans=random.randint(0,3)
for a in range(3):
    print(a+1,"번째 판!!!")
    print("가위바위보!")
    x=int(input("0:주먹, 1:가위, 2:보 ="))
    com_ans=int(random.random()*3)

    if x==0:
        if com_ans==0:
            print("무승부")
            d+=1
        elif com_ans==1:
            print("승리!")
            w += 1
        else:
            print("패배!")
            r += 1
    elif x==1:
        if com_ans==1:
            print("무승부")
            d += 1
        elif com_ans==2:
            print("승리!")
            w += 1
        else:
            print("패배!")
            r += 1
    else:
        if com_ans==2:
            print("무승부")
            d += 1
        elif com_ans==0:
            print("승리!")
            w += 1
        else:
            print("패배!")
            r += 1
total=w+r+d
print("총전적 {}전 {}승 {}무 {}패".format(total,w,d,r) )
print("승률 :",int(w*100/total),"%")