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
        vr_test=[["audi", a1],["chevrolet", a2],["dodge", a3],["ford", a4],["honda", a5],["hyundai", a6],
                 ["jeep", a7],["land rover", a8],["lincoln", a9],["mercury", a10],["nissan", a11],["pontiac", a12],
                 ["subaru", a13],["toyota", a14],["volkswagen", a15]]
        break
    vr_data = line.split(",")
    b=vr_data[2].split(("."))
    c=int(b[0])

    if vr_data[0]=="audi":
        if vr_data[10]=="compact\n":
            a1+=1
    if vr_data[0]=="chevrolet":
        if vr_data[10]=="compact\n":
            a2+=1
    if vr_data[0]=="dodge":
        if vr_data[10]=="compact\n":
            a3+=1
    if vr_data[0]=="ford":
        if vr_data[10]=="compact\n":
            a4+=1
    if vr_data[0]=="honda":
        if vr_data[10]=="compact\n":
            a5+=1
    if vr_data[0]=="hyundai":
        if vr_data[10]=="compact\n":
            a6+=1
    if vr_data[0]=="jeep":
        if vr_data[10]=="compact\n":
            a7+=1
    if vr_data[0]=="land rover":
        if vr_data[10]=="compact\n":
            a8+=1
    if vr_data[0]=="lincoln":
        if vr_data[10]=="compact\n":
            a9+=1
    if vr_data[0]=="mercury":
        if vr_data[10]=="compact\n":
            a10+=1
    if vr_data[0]=="nissan":
        if vr_data[10]=="compact\n":
            a11+=1
    if vr_data[0]=="pontiac":
        if vr_data[10]=="compact\n":
            a12+=1
    if vr_data[0]=="subaru":
        if vr_data[10]=="compact\n":
            a13+=1
    if vr_data[0]=="toyota":
        if vr_data[10]=="compact\n":
            a14+=1
    if vr_data[0]=="volkswagen":
        if vr_data[10]=="compact\n":
            a15+=1
    # vr_list.append(vehicle(vr_data[0],vr_data[1],vr_data[2],int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()

result = reversed(sorted(vr_test, key=lambda vr_test: vr_test[1]))

idx = 1

for tmp in result:
    print("{}".format(tmp))
    idx += 1


# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.