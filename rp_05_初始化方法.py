class Cat:
    def __init__(self):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        self.name = "Jerry"


# 使用类名()创建一个对象的时候, 会自动调用初始化方法:
tom = Cat()
print("这一个猫咪的名字是 %s" % tom.name)
