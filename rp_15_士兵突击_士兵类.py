# 士兵许三多有一把AK47
# 士兵可以开火
# 枪能够发射子弹
# 枪装填子弹 -- 增加子弹数量
class Gun:
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def fire(self):
        self.bullet_count -= 1


class Solder:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def trigger(self, gun):
        if self.gun.bullet_count > 0:
            self.gun.fire()
            print("%s扣动了扳机, %s发射了一发子弹"
              % (self.name, self.gun.model))
        else:
            print("长官, %s已经弹尽粮绝" % self.name)


AK47 = Gun("AK47", 100)
xusando = Solder("许三多", AK47)

for i in range(101):
    xusando.trigger(AK47)


print("现在%s里还有%d发子弹" %
      (xusando.gun.model, xusando.gun.bullet_count))
