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
vr_hwy8=0
vr_hwy9=0
vr_hwy10=0
vr_hwy11=0
vr_hwy12=0
vr_hwy13=0
vr_hwy14=0
vr_hwy15=0
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
a10=0
a11=0
a12=0
a13=0
a14=0
a15=0
vr_test=list()
while True:
    line = file.readline()
    if not line:
        vr_test=[["audi", vr_hwy1/a1],["chevrolet", vr_hwy2/a2],["dodge", vr_hwy3/a3],["ford", vr_hwy4/a4],["honda", vr_hwy5/a5],["hyundai", vr_hwy6/a6],
                 ["jeep", vr_hwy7/a7],["land rover", vr_hwy8/a8],["lincoln", vr_hwy9/a9],["mercury", vr_hwy10/a10],["nissan", vr_hwy11/a11],["pontiac", vr_hwy12/a12],
                 ["subaru", vr_hwy13/a13],["toyota", vr_hwy14/a14],["volkswagen", vr_hwy15/a15]]
        break
    vr_data = line.split(",")
    b=vr_data[2].split(("."))
    c=int(b[0])

    if vr_data[0]=="audi":
        vr_hwy1+=int(vr_data[8])
        a1+=1
    if vr_data[0]=="chevrolet":
        vr_hwy2+=int(vr_data[8])
        a2 += 1
    if vr_data[0]=="dodge":
        vr_hwy3+=int(vr_data[8])
        a3 += 1
    if vr_data[0]=="ford":
        vr_hwy4+=int(vr_data[8])
        a4 += 1
    if vr_data[0]=="honda":
        vr_hwy5+=int(vr_data[8])
        a5 += 1
    if vr_data[0]=="hyundai":
        vr_hwy6+=int(vr_data[8])
        a6 += 1
    if vr_data[0]=="jeep":
        vr_hwy7+=int(vr_data[8])
        a7 += 1
    if vr_data[0]=="land rover":
        vr_hwy8+=int(vr_data[8])
        a8 += 1
    if vr_data[0]=="lincoln":
        vr_hwy9+=int(vr_data[8])
        a9 += 1
    if vr_data[0]=="mercury":
        vr_hwy10+=int(vr_data[8])
        a10 += 1
    if vr_data[0]=="nissan":
        vr_hwy11+=int(vr_data[8])
        a11 += 1
    if vr_data[0]=="pontiac":
        vr_hwy12+=int(vr_data[8])
        a12 += 1
    if vr_data[0]=="subaru":
        vr_hwy13+=int(vr_data[8])
        a13 += 1
    if vr_data[0]=="toyota":
        vr_hwy14+=int(vr_data[8])
        a14 += 1
    if vr_data[0]=="volkswagen":
        vr_hwy15+=int(vr_data[8])
        a15 += 1
    # vr_list.append(vehicle(vr_data[0],vr_data[1],vr_data[2],int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()

result = reversed(sorted(vr_test, key=lambda vr_test: vr_test[1]))

idx = 1

for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1
    if idx ==4:
        break

# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.