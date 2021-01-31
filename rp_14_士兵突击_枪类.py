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


AK47 = Gun("AK47", 99)
print("%s 有 %d发子弹" % (AK47.model, AK47.bullet_count))
