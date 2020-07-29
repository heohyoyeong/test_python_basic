# 객체지향을 하는 이유는 => 유지보수와 재사용성
# 재사용성을 위한 대표적인 객체지향 기법 => inheritance(상속)
# parent class, super class (부모 클래스) = >  child class, sub class (자식 클래스)
# is-A 관계 (subclass is a super class)의 약자


# 두개의 class를 이용
# unit class와 marin class
# unit class => 모든 unit이 공통으로 가지고 있는 속성과 method로 구성
#               super class로 사용, base class
# marin => sub class

# python의 모든 class는 object class이다!=> python의 모든 class는 object class를 상속한다.

# class unit(object): #super class
#
#     def __init__(self,damage,life):
#         self.utype= self.__class__.__name__
#         self.damage=damage
#         self.life=life
#
#     def show_status(self):
#         print(f"직업 : {self.utype}")
#         print(f"공격력 : {self.damage}")
#         print(f"생명력 : {self.life}")
#
# class Marine(unit): #sub class
#
#     def __init__(self,damage,life,range_upgrade,stim_upgrade):
#         super(Marine, self).__init__(damage,life)
#         self.range_upgrade=range_upgrade
#         self.stim_upgrade = stim_upgrade
#
#     def show_status(self):
#         super(Marine, self).show_status()
#         print(f"사거리 업그레이드 유무 : {self.range_upgrade}")
#         print(f"스팀팩 업그레이드 유무 : {self.stim_upgrade}")
#
#
#     def use_stim(self):
#         if self.stim_upgrade==False:
#             return print("스팀팩 사용불가능")
#         else:
#             self.life -=10
#             print(f"스팀팩 사용 현재 체력 {self.life}")


# m1=Marine(5,40,True,True)
#
# m1.show_status()
# m1.use_stim()
# m1.use_stim()
# m1.use_stim()
# m1.use_stim()

###################################################################################

#사용할 유닛들은 Marine, Medic, Vulture, Dropship 4종류 유닛

class unit(object): #super class

    def __init__(self,damage,life):
        self.utype= self.__class__.__name__
        self.damage=damage
        self.life=life

    def show_status(self):
        print(f"직업 : {self.utype}")
        print(f"공격력 : {self.damage}")
        print(f"생명력 : {self.life}")


    def attack(self):
        pass

class Marine(unit):
    #overriding
    def __init__(self,damage,life,range_upgrade):
        super(Marine,self).__init__(damage,life)
        self.range_upgrade =range_upgrade

    # overriding
    def show_status(self):
        super(Marine, self).show_status()
        print(f"사거리 업그레이드 유무: {self.range_upgrade}")

    # overriding
    def attack(self):
        print("마린이 총으로 공격합니다. 땅땅!!!!")


    def stimpack(self):
        if int(self.life) < 20:
            print("체력이 작아서 수행이 불가능합니다.")
        else:
            # self.life -=10
            # self.damage *=1.5
            print("마린이 스팀팩을 사용합니다! oh yeah!! fire! ")

class Madic(unit):

    #overriding
    def attack(self):
        print("메딕이 치료합니다. 힐힐!!!")

class Vulture(unit):

    def __init__(self,damage,life,amount_of_mine):
        super(Vulture, self).__init__(damage,life)
        self.amount_of_mine =amount_of_mine

    def attack(self):
        print("벌쳐가 공격합니다. ~~~~")


class Dropship(unit):

    # overriding
    def attack(self,location):
        print(f"{location}로 이동합니다.  슝!!")

    def board(self,unit_list):
        self.unit_list = unit_list
        print("유닛들을 드랍쉽에 태워요.")

    def drop(self):
        print("모든 unit이 드랍쉽에서 내립니다.")
        return self.unit_list


#마린을 3마리나 생성합니다.
m1=Marine(100,100,False)
m2=Marine(100,100,False)
m3=Marine(100,100,False)

#메딕을 3마리나 생성합니다.

me=Madic(0,100)

#벌쳐 2마리생성

v1=Vulture(200,100,3)
v2=Vulture(200,100,3)

army=list()
army.append(m1)
army.append(m2)
army.append(m3)
army.append(me)
army.append(v1)
army.append(v2)

d=Dropship(0,5000)

d.board(army)

d.attack("아군 기지")

my_list=d.drop()
print(my_list)

for unit in my_list:
    if isinstance(unit.Marine):
        pass
    unit.attack()


# m1.show_status()
# m1.stimpack()
#
# m1.show_status()
