#각 사람에 대한 데이터를 읽어서 성적순으로 출력
#1등 아이유 95.6<-평균
#3등 최길동 88.2...
import statistics as st

file1= open("C:/python_data/student_score.txt","r")
a=list()
while True:
    line= file1.readline()
    if not line:
        break
    b=line.split(",")
    a.append(b)
file1.close()


ff=list()
score=list()
names=list()


for k in range(0,7):
    name=a[k][0]
    c= int(a[k][1])
    d= int(a[k][2])
    e= int(a[k][3])
    aver=(c+d+e)/3
    ff.append(aver)
    # print(f"이름: {name} 평균: {aver}")
    if aver== max(ff):
        score.insert(0,aver)
        names.insert(0,name)
    elif aver== min(ff):
        score.append(aver)
        names.append(name)

print(score)
print(names)