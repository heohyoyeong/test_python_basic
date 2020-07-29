class Student(object):
    def __init__(self,name,kor,eng,math):
        self.__name=name
        self.__kor=kor
        self.__eng=eng
        self.__math=math
        self.avg=(eng+kor+math)/3

    def __repr__(self):
        return "{} {}".format(self.__name,self.avg)


file1= open("C:/python_data/student_score.txt","r")

a=list()

while True:
    line= file1.readline()
    if not line:
        break
    b=line.split(",")
    a.append(Student(b[0],int(b[1]),int(b[2]),int(b[3])))
file1.close()


result= sorted(a,key=lambda b: b.avg)

for tmp in result:
    print(tmp)

d=reversed(result)

print(d)

for s in range(1,8):
    print("{}등 {} {}".format(s,d[0][0],d[0][1]))