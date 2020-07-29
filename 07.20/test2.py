class vehicle(object):
    def __init__(self,car_data):
        car_data=car_data.split(",")
        self.manufacturer=car_data[0]
        self.model=car_data[1]
        self.displ=float(car_data[2])
        self.year=int(car_data[3])
        self.cyl=int(car_data[4])
        self.trans=car_data[5]
        self.drv=car_data[6]
        self.cty=int(car_data[7])
        self.hwy=int(car_data[8])
        self.fl=car_data[9]
        self.cl=car_data[10]

    def __repr__(self):
        return self.manufacturer+","+self.model+","+self.displ+","+self.year+","+self.cyl+","+self.trans+","+self.drv+","+self.hwy+","+self.fl+","+self.cl

#

file=open("C:/python_data/mpg.txt","r")

vr_list=list()
vr_hwy1=0
vr_hwy2=0
a1=0
a2=0
while True:
    line = file.readline()
    if not line:
        print(f"아우디의 연비 {vr_hwy1/a1}")
        print(f"토요타의 연비 {vr_hwy2/a2}")
        break
    vr_data = line.split(",")
    b=vr_data[2].split(("."))
    c=int(b[0])
    if vr_data[0]=="audi":
        vr_hwy1+=int(vr_data[7])
        a1+=1
    if vr_data[0]=="toyota":
        vr_hwy2+=int(vr_data[7])
        a2 += 1
    # vr_list.append(vehicle(vr_data[0],vr_data[1],c,int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()


# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.