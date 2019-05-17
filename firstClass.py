import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl       # 멤버 변수
        self.atkh = atkh       # 멤버 변수

    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("HP is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()


'''
while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strkes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp > 30:
        # continue문 이후의 print문은 실행 안됨
        continue

    print('You have low helath. You have veen teleported to the nearest inn.')
    break
'''