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
        if a1==0:
            a1=1
        if a2==0:
            a2=1
        if a3==0:
            a3=1
        if a4==0:
            a4=1
        if a5==0:
            a5=1
        if a6==0:
            a6=1
        if a7==0:
            a7=1
        if a8==0:
            a8=1
        if a9==0:
            a9=1
        if a10==0:
            a10=1
        if a11==0:
            a11=1
        if a12==0:
            a12=1
        if a13==0:
            a13=1
        if a14==0:
            a14=1
        if a15==0:
            a15=1
        vr_test=[["audi", vr_hwy1/a1],["chevrolet", vr_hwy2/a2],["dodge", vr_hwy3/a3],["ford", vr_hwy4/a4],["honda", vr_hwy5/a5],["hyundai", vr_hwy6/a6],
                 ["jeep", vr_hwy7/a7],["land rover", vr_hwy8/a8],["lincoln", vr_hwy9/a9],["mercury", vr_hwy10/a10],["nissan", vr_hwy11/a11],["pontiac", vr_hwy12/a12],
                 ["subaru", vr_hwy13/a13],["toyota", vr_hwy14/a14],["volkswagen", vr_hwy15/a15]]
        break
    vr_data = line.split(",")
    b=vr_data[2].split(("."))
    c=int(b[0])

    if vr_data[0]=="audi":
        if vr_data[10]=="suv\n":
            vr_hwy1+=(int(vr_data[8])+int(vr_data[7]))
            a1+=1
    if vr_data[0]=="chevrolet":
        if vr_data[10]=="suv\n":
            vr_hwy2+=(int(vr_data[8])+int(vr_data[7]))
            a2+=1
    if vr_data[0]=="dodge":
        if vr_data[10]=="suv\n":
            vr_hwy3+=(int(vr_data[8])+int(vr_data[7]))
            a3+=1
    if vr_data[0]=="ford":
        if vr_data[10]=="suv\n":
            vr_hwy4+=(int(vr_data[8])+int(vr_data[7]))
            a4+=1
    if vr_data[0]=="honda":
        if vr_data[10]=="suv\n":
            vr_hwy5+=(int(vr_data[8])+int(vr_data[7]))
            a5+=1
    if vr_data[0]=="hyundai":
        if vr_data[10]=="suv\n":
            vr_hwy6+=(int(vr_data[8])+int(vr_data[7]))
            a6+=1
    if vr_data[0]=="jeep":
        if vr_data[10]=="suv\n":
            vr_hwy7+=(int(vr_data[8])+int(vr_data[7]))
            a7+=1
    if vr_data[0]=="land rover":
        if vr_data[10]=="suv\n":
            vr_hwy8+=(int(vr_data[8])+int(vr_data[7]))
            a8+=1
    if vr_data[0]=="lincoln":
        if vr_data[10]=="suv\n":
            vr_hwy9+=(int(vr_data[8])+int(vr_data[7]))
            a9+=1
    if vr_data[0]=="mercury":
        if vr_data[10]=="suv\n":
            vr_hwy10+=(int(vr_data[8])+int(vr_data[7]))
            a10+=1
    if vr_data[0]=="nissan":
        if vr_data[10]=="suv\n":
            vr_hwy11+=(int(vr_data[8])+int(vr_data[7]))
            a11+=1
    if vr_data[0]=="pontiac":
        if vr_data[10]=="suv\n":
            vr_hwy12+=(int(vr_data[8])+int(vr_data[7]))
            a12+=1
    if vr_data[0]=="subaru":
        if vr_data[10]=="suv\n":
            vr_hwy13+=(int(vr_data[8])+int(vr_data[7]))
            a13+=1
    if vr_data[0]=="toyota":
        if vr_data[10]=="suv\n":
            vr_hwy14+=(int(vr_data[8])+int(vr_data[7]))
            a14+=1
    if vr_data[0]=="volkswagen":
        if vr_data[10]=="suv\n":
            vr_hwy15+=(int(vr_data[8])+int(vr_data[7]))
            a15+=1
    vr_list.append(vehicle(vr_data[0],vr_data[1],vr_data[2],int(vr_data[3]),int(vr_data[4]),vr_data[5],vr_data[6],int(vr_data[7]),int(vr_data[8]),vr_data[9],vr_data[10]))

file.close()

result = reversed(sorted(vr_test, key=lambda vr_test: vr_test[1]))

idx = 1

for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1
    if idx ==6:
        break
# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.