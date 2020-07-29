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
        return "모델명 :{} 고속도로연비: {} ".format(self.model, self.hwy)

file=open("C:/python_data/mpg.txt","r")
vr_list=list()
# vr_list2=list()
# vr_list3=list()

while True:
    line = file.readline()
    if not line:
        vr_
        break
    vr_data = line.split(",")
    if vr_data[0]=="audi":
        vr_list.append(vehicle(vr_data[0],vr_data[1],vr_data[2],int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))
        # if vr_data[1]=="a4 quattro":
        #     vr_list2.append(
        #         vehicle(vr_data[0], vr_data[1], vr_data[2], int(vr_data[3]), int(vr_data[4]), vr_data[5], vr_data[6],
        #                 int(vr_data[7]), int(vr_data[8]), vr_data[9], vr_data[10]))
        # if vr_data[1]=="a6 quattro":
        #     vr_list3.append(
        #         vehicle(vr_data[0], vr_data[1], vr_data[2], int(vr_data[3]), int(vr_data[4]), vr_data[5], vr_data[6],
        #                 int(vr_data[7]), int(vr_data[8]), vr_data[9], vr_data[10]))



file.close()


result = reversed(sorted(vr_list, key=lambda vehicle: vehicle.hwy))

idx = 1
for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.
