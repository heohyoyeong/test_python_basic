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
vr_list1=list()
vr_list2=list()
vr_list3=list()
a1=0
a2=0
a3=0
p1=0
p2=0
p3=0

while True:
    line = file.readline()
    if not line:
        vr_test=(["a4", a1/p1],["a4 quattro", a2/p2],["a6 quattro", a3/p3])
        break
    vr_data = line.split(",")
    if vr_data[0]=="audi":
        if vr_data[1]=="a4 quattro":
            vr_list2.append(
                vehicle(vr_data[0], vr_data[1], vr_data[2], int(vr_data[3]), int(vr_data[4]), vr_data[5], vr_data[6],
                        int(vr_data[7]), int(vr_data[8]), vr_data[9], vr_data[10]))
            a2+=int(vr_data[8])
            p2+=1
        if vr_data[1]=="a6 quattro":
            vr_list3.append(
                vehicle(vr_data[0], vr_data[1], vr_data[2], int(vr_data[3]), int(vr_data[4]), vr_data[5], vr_data[6],
                        int(vr_data[7]), int(vr_data[8]), vr_data[9], vr_data[10]))
            a3 += int(vr_data[8])
            p3 += 1
        if vr_data[1]=="a4":
            vr_list1.append(
                vehicle(vr_data[0], vr_data[1], vr_data[2], int(vr_data[3]), int(vr_data[4]), vr_data[5], vr_data[6],
                        int(vr_data[7]), int(vr_data[8]), vr_data[9], vr_data[10]))
            a1 += int(vr_data[8])
            p1 += 1


file.close()


result = reversed(sorted(vr_test, key=lambda vr_test: vr_test[1]))

idx = 1
for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.
