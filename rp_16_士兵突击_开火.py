# 士兵许三多有一把AK47
# 士兵可以开火
# 枪能够发射子弹
# 枪装填子弹 -- 增加子弹数量
class Gun:
    def __init__(self, model):
        # 1. 枪的型号
        self.model = model
        # 2. 子弹的数量为零
        self.bullet_count = 0

    def reload(self, count):
        self.bullet_count += count

    def fire(self):
        if self.bullet_count <= 0:
            print("残念, [%s]没有子弹了..." % self.model)
            return
        self.bullet_count -= 1
        print(" [%s]突突突~~ [%d]"
              % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 1. 姓名
        self.name = name
        # 2. 枪 --新兵没有枪
        self.gun = None

    def trigger(self):
        # 1.判断士兵是否有枪? is 身份运算符用来判断变量的地址是否相等
        if self.gun is None:
            print("长官, [%s] 还没有枪, 烧火棍凑活一下?" % self.name)
            return
        # 2. 高喊口号
        print("冲啊..[%s]!" % self.name)
        # 3. 让枪装填子弹
        self.gun.reload(50)
        # 4. 让枪发射子弹
        if self.gun.bullet_count > 0:
            self.gun.fire()
            print("%s扣动了扳机, %s发射了一发子弹"
                  % (self.name, self.gun.model))
        else:
            print("长官, %s已经弹尽粮绝" % self.name)


# 1. 创建枪对象
ak47 = Gun("AK47")
xusando = Soldier("许三多")
xusando.gun = ak47
xusando.trigger()

print(xusando)
print("现在%s里还有%d发子弹" %
      (xusando.gun.model, xusando.gun.bullet_count))
