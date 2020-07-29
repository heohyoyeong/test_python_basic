class vehicle(object):
    def __init__(self,manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,cl):
        self.manufacturer=manufacturer
        self.model=model
        self.displ=displ
        self.year=year
        self.cyl=cyl
        self.trans=trans
        self.drv=drv
        self.cty=cty
        self.hwy=hwy
        self.fl=fl
        self.cl=cl

    def __repr__(self):
        return "{} {} {}".format(self.model, self.displ, self.hwy)

file=open("C:/python_data/mpg.txt","r")

vr_list=list()
vr_hwy1=0
vr_hwy2=0
vr_hwy3=0
a1=0
a2=0
a3=0
while True:
    line = file.readline()
    if not line:
        print(f"쉐보레의 연비 {vr_hwy1/a1}")
        print(f"포드의 연비 {vr_hwy2/a2}")
        print(f"혼다의 연비 {vr_hwy3/a3}")
        break
    vr_data = line.split(",")
    b=vr_data[2].split(("."))
    c=int(b[0])
    if vr_data[0]=="chevrolet":
        vr_hwy1+=int(vr_data[8])
        a1+=1
    if vr_data[0]=="ford":
        vr_hwy2+=int(vr_data[8])
        a2 += 1
    if vr_data[0]=="honda":
        vr_hwy3+=int(vr_data[8])
        a3 += 1
    # vr_list.append(vehicle(vr_data[0],vr_data[1],c,int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()


# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
