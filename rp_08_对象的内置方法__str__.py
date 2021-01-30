class Cat:
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "这是一只懒猫 [%s]" % self.name

    def __del__(self):
        print("%s 我去了" % self.name)


# tom是一个全局变量
tom = Cat("Tom")
print(tom)
