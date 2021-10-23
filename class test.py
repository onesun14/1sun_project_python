#hp, mp
import random
class makeCh():

    def __init__(self):
        self.hp = random.randrange(100, 150)
        self.mp = random.randrange(170, 200)
        self.str = random.randrange(10, 50)

    def hit(self):
        return self.str

    def sword_skill(self):
        return self.str * 2

    def magic_skill(self):
        return self.str + self.mp

#sword_skill 공격력의 2배 만큼 데미지를 넣는다.
#magic_skill 공격력과 마나량을 더한 만큼 데미지를 넣는다.


a = makeCh()
print("검사 character hp : {} , mp : {}, str : {}".format(a.hp, a.mp, a.str))

b = makeCh()
print("마법사 character hp : {} , mp : {}, str : {}".format(b.hp, b.mp, b.str))

a_Damage = 0
b_Damage = 0
#스킬을 쓸수 있다면 쓰고 아니면 일반 공격하며 mp를 채운다.

def a_battle(a_num):
    a_default_Damage = random.randrange ( a.str )
    if a_num == "스킬":
        if a.mp >= 75:
            b.hp = b.hp - a.sword_skill()
            print ( "------------------" )
            print("마나 사용 -75")
            print("검사는 약점찌르기를 사용했다! 입힌 데미지 : {}".format(a.sword_skill()))
            print("현재 검사는 character hp : {} , mp : {},".format(a.hp, a.mp,))
            print("현재 마법사는 character hp : {} , mp : {}, 받은 데미지 : {}".format(b.hp, b.mp, a.sword_skill()))
            print ( "------------------" )
        elif a.mp <= 75:
            print ( "------------------" )
            print("마나가 없다!")
            b.hp = b.hp - a.hit()
            a.mp += 20
            print("마법사의 일반 공격")
            print("검사 마나 회복 +20")
            print("현재 검사는 character hp : {} , mp : {}".format(a.hp, a.mp))
            print("현재 마법사는 character hp : {} , mp : {}, 받은 데미지 : {}".format(b.hp, b.mp, a_default_Damage))
            print ( "------------------" )
    elif a_num == "공격":
        b.hp = b.hp - a.hit()
        a.mp += 20
        print ( "------------------" )
        print("마법사의 일반 공격")
        print("검사 마나 회복 +20")
        print("현재 검사는 character hp : {} , mp : {}".format(a.hp, a.mp))
        print("현재 마법사는 character hp : {} , mp : {}, 받은 데미지 : {}".format(b.hp, b.mp, a_default_Damage))
        print ( "------------------" )

def b_battle(b_num):
    b_default_Damage = random.randrange ( b.str )
    if b_num == "스킬":
        if b.mp >= 50:
            a.hp = a.hp - b.magic_skill()
            print ( "------------------" )
            print("마나 사용 -50")
            print("마법사는 마법 공격을 사용했다! 입힌 데미지 : {}".format(b.magic_skill()))
            print("현재 검사는 character hp : {} , mp : {}, 받은 데미지 : {}".format(a.hp, a.mp, b.magic_skill()))
            print("현재 마법사는 character hp : {} , mp : {}".format(b.hp, b.mp))
            print ( "------------------" )
        elif a.mp <= 50:
            print ( "------------------" )
            print("마나가 없다!")
            a.hp = a.hp - b.hit()
            b.mp += 20
            print("마법사의 일반 공격")
            print("마법사 마나 회복 +20")
            print("현재 검사는 character hp : {} , mp : {}, 받은 데미지 : {}".format(a.hp, a.mp, b_default_Damage))
            print("현재 마법사는 character hp : {} , mp : {}".format(b.hp, b.mp))
            print ( "------------------" )
    elif a_num == "공격":
        a.hp = a.hp - b.hit ()
        b.mp += 20
        print("------------------")
        print ( "마법사의 일반 공격" )
        print ( "마법사 마나 회복 +20" )
        print ( "현재 검사는 character hp : {} , mp : {}, 받은 데미지 : {}".format ( a.hp, a.mp, b_default_Damage ) )
        print ( "현재 마법사는 character hp : {} , mp : {}".format ( b.hp, b.mp ) )
        print("------------------")

while a.hp >= 0 and b.hp >= 0:
    a_num = input ( "공격 or 스킬(mp 75소모) : " )
    if a_num != '공격' and a_num != '스킬':
        print('공격 or 스킬(mp 75소모) 중에 고르세요 : ')
    elif a_num =='공격' or a_num == '스킬':
        a_battle(a_num)
    b_num = input ( "공격 or 스킬(mp 50소모) : " )
    if b_num != '공격' and b_num != '스킬' :
        print ( '공격 or 스킬(mp 50소모) 중에 고르세요 : ' )
    elif b_num == '공격' or b_num == '스킬' :
        b_battle(b_num)



if a.hp >= 0:
    print("a win")
else:
    print("b win")
