class Person:
    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 我的体重是 %.2f " % (self.name, self.weight)

    def run(self):
        pass

    def eat(self):
        pass


xiaoming = Person("小明", 75)

xiaoming.run()

xiaoming.eat()

print(xiaoming)
