class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)
