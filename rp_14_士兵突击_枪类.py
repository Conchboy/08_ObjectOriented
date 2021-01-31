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


ak47 = Gun("AK47")
ak47.reload(55)
ak47.fire()
print("%s 还有 %d发子弹" % (ak47.model, ak47.bullet_count))
