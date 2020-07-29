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
vr_hwy4=0
vr_hwy5=0
vr_hwy6=0
vr_hwy7=0
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
vr_test=list()
while True:
    line = file.readline()
    if not line:
        vr_test=[["compact", vr_hwy1/a1],["midsize", vr_hwy2/a2],["suv", vr_hwy3/a3],["pickup", vr_hwy4/a4],["subcompact", vr_hwy5/a5],["minivan", vr_hwy6/a6],["2seater", vr_hwy7/a7]]
        break
    vr_data = line.split(",")
    b=vr_data[2].split(("."))
    c=int(b[0])

    if vr_data[10]=="compact\n":
        vr_hwy1+=int(vr_data[7])
        a1+=1
    if vr_data[10]=="midsize\n":
        vr_hwy2+=int(vr_data[7])
        a2 += 1
    if vr_data[10]=="suv\n":
        vr_hwy3+=int(vr_data[7])
        a3 += 1
    if vr_data[10]=="pickup\n":
        vr_hwy4+=int(vr_data[7])
        a4 += 1
    if vr_data[10]=="subcompact\n":
        vr_hwy5+=int(vr_data[7])
        a5 += 1
    if vr_data[10]=="minivan\n":
        vr_hwy6+=int(vr_data[7])
        a6 += 1
    if vr_data[10]=="2seater\n":
        vr_hwy7+=int(vr_data[7])
        a7 += 1
    vr_list.append(vehicle(vr_data[0],vr_data[1],vr_data[2],int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()
result = reversed(sorted(vr_test, key=lambda vr_test: vr_test[1]))

idx = 1

for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1


# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.