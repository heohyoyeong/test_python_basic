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

file=open("C:/python_data/mpg.txt","r")

vr_list=list()
while True:
    line = file.readline()
    if not line:
        break
    vr_list.append(vehicle(line.strip()))

file.close()
######################################################

displ_4_lower = []
displ_5_upper = []

for tmp in vr_list:
    if tmp.displ <=4:
        displ_4_lower.append(tmp.hwy)
    elif tmp.displ >= 5:
        displ_5_upper.append(tmp.hwy)

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))



# displ_4_lower_list = list(filter(lambda tmp:tmp.displ <= 4,car_list))
# displ_5_upper_list = list(filter(lambda tmp:tmp.displ >= 5,car_list))
#
# displ_4_lower = [tmp.hwy for tmp in displ_4_lower_list]
# displ_5_upper = [tmp.hwy for tmp in displ_5_upper_list]
#
# avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
# avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)
#
# print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
# print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))


    # 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
    # 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.


# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

