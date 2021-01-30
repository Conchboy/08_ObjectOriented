class Cat:
    def __init__(self, name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        self.name = name
    def eat(self):
        # 那一个对象调用的方法, self就是那一个对象的引用
        print("小猫%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫%s爱喝水" % self.name)


tom = Cat("Tom")
# 对象的属性在类定义外定义, 不推荐
# tom.name = "Tom"

tom.eat()
tom.drink()
# tom.name = "Tom"
