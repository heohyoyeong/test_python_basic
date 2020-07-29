# ROCK=0
# SCISSORS=1
# PAPER=2

import random

# com_ans=random.randint(0,3)

com_ans=int(random.random()*3)

com_ans=(int(random.random()*10))%3

print("내꺼! 가위바위보!")
x=int(input("0:주먹, 1:가위, 2:보 ="))

if x==0:
    if com_ans==0:
        print("무승부")
    elif com_ans==1:
        print("승리!")
    else:
        print("패배!")
elif x==1:
    if com_ans==1:
        print("무승부")
    elif com_ans==2:
        print("승리!")
    else:
        print("패배!")
else:
    if com_ans==2:
        print("무승부")
    elif com_ans==0:
        print("승리!")
    else:
        print("패배!")



