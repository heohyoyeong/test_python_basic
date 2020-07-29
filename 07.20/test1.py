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
a1=0
a2=0


while True:
    line = file.readline()
    if not line:
        print(f"4이하의 결과값 {vr_hwy1/a1}")
        print(f"5이상의 결과값 {vr_hwy2/a2}")
        break
    vr_data = line.split(",")
    if float(vr_data[2])<=4:
        vr_hwy1+=int(vr_data[8])
        a1+=1
    if float(vr_data[2])>=5:
        vr_hwy2+=int(vr_data[8])
        a2 += 1
    vr_list.append(vehicle(vr_data[0],vr_data[1],float(vr_data[2]),int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()


# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
