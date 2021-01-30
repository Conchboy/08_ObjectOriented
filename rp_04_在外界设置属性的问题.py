class Cat:
    def eat(self):
        print("小猫%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫%s爱喝水" % self.name)


tom = Cat()
# 对象的属性在类定义外定义, 不推荐
tom.name = "Tom"

lazy_cat = Cat()
lazy_cat.name = "大懒猫"

lazy_cat2 = lazy_cat

tom.eat()
tom.drink()
lazy_cat.eat()
lazy_cat.drink()
print(tom)
print(lazy_cat)
print(lazy_cat2)
addr = id(tom)
print("%x" % addr)
