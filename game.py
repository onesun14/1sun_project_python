import random
class makeCh():

    def __init__(self):
        self.hp = random.randrange(100, 300)
        self.mp = random.randrange(170, 200)
        self.str = random.randrange(10, 100)

    def hit(self):
        return self.str

    def sword_skill(self):
        return "검사", "약점찌르기", self.str * 3, 75

    def magic_skill(self):
        return "마법사", "파이어볼", (self.str + self.mp)//2 , 50

#sword_skill 공격력의 3배 만큼 데미지를 넣는다.
#magic_skill 공격력과 마나량을 더한 만큼 데미지를 넣는다.


sword_man = makeCh()
print("sword_man hp : {} , mp : {}, str : {}".format(sword_man.hp, sword_man.mp, sword_man.str))

Wizard = makeCh()
print("Wizard hp : {} , mp : {}, str : {}".format(Wizard.hp, Wizard.mp, Wizard.str))

def Skill(sequence, Enemy):
    if sequence == sword_man:
        name, skill, damage, mp = sequence.sword_skill()
        Enemy_name, Enemy_skill, Enemy_damage, Enemy_mp = Enemy.magic_skill()
    else:
        name, skill, damage, mp = sequence.magic_skill()
        Enemy_name, Enemy_skill, Enemy_damage, Enemy_mp = Enemy.sword_skill()
    print("------------------")
    print("마나 사용 -{}".format(mp))
    cri = random.randrange(1, 5)
    if cri == 1:
        Enemy.hp -= damage * 2
        print("크리티컬!")
    else:
        Enemy.hp -= damage
    print("{}는 {} 사용했다! 입힌 데미지 : {}".format(name, skill, damage))
    print("현재 {}는 hp : {} , mp : {},".format(name, sequence.hp, sequence.mp))
    if sequence == sword_man:
        sequence = Wizard
    else:
        sequence = sword_man
    print("현재 {}는 hp : {} , mp : {}, 받은 데미지 : {}".format(Enemy_name, sequence.hp, sequence.mp, damage))
    print("------------------")

def Attack(sequence, Enemy):
    default_Damage = random.randrange(sequence.str)
    cri = random.randrange(1, 5)
    if sequence == sword_man:
        name, skill, damage, mp = sequence.sword_skill()
        Enemy_name, Enemy_skill, Enemy_damage, Enemy_mp = Enemy.magic_skill()
    else:
        name, skill, damage, mp = sequence.magic_skill()
        Enemy_name, Enemy_skill, Enemy_damage, Enemy_mp = Enemy.sword_skill()
    if cri <= 1:
        Enemy.hp -= default_Damage * 2
        print("크리티컬!")
    else:
        Enemy.hp -= default_Damage
    sequence.mp += 20
    print("------------------")
    print("{}의 일반 공격".format(name))
    print("{} 마나 회복 +20".format(name))
    print("현재 {}는 hp : {} , mp : {}".format(name, sequence.hp, sequence.mp))
    if sequence == sword_man:
        sequence = Wizard
    else:
        sequence = sword_man
    print("현재 {}는 hp : {} , mp : {}, 받은 데미지 : {}".format(Enemy_name, sequence.hp, sequence.mp, default_Damage))
    print("------------------")


#스킬을 쓸수 있다면 쓰고 아니면 일반 공격하며 mp를 채운다.

while sword_man.hp >= 0 and Wizard.hp >= 0:
    num = input ( "공격 or 스킬(mp 75소모) : " )
    if num != '공격' and num != '스킬':
        print('공격 or 스킬(mp 75소모) 중에 고르세요 : ')
    elif num =='공격' or num == '스킬':
        if num =='스킬':
            if sword_man.mp >= 75:
                Skill(sword_man, Wizard)
            else:
                print("마나가 부족하다!")
                Attack(sword_man, Wizard)
        elif num =='공격':
            Attack(sword_man, Wizard)
    if sword_man.hp <= 0 or Wizard.hp <= 0:
        break
    if Wizard.mp >= 50:
        Skill(Wizard, sword_man)
    else:
        print("마나가 부족하다!")
        Attack(Wizard, sword_man)






if sword_man.hp >= 0:
    print("sword_man win")
else:
    print("Wizard win")
