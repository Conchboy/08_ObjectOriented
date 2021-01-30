class Cat:
    def eat(self):
        # 那一个对象调用的方法, self就是那一个对象的引用
        print("小猫%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫%s爱喝水" % self.name)


tom = Cat()
# 对象的属性在类定义外定义, 不推荐
# tom.name = "Tom"

tom.eat()
tom.drink()
tom.name = "Tom"
