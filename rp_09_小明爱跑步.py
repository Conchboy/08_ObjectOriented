class Person:
    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 我的体重是 %.2f " % (self.name, self.weight)

    def run(self):
        print(" %s 爱跑步,跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print(" %s 爱吃鸡腿,吃鸡腿让人心情舒畅" % self.name)
        self.weight += 0.75


xiaoming = Person("小明", 75)

xiaoming.run()

xiaoming.eat()

print(xiaoming)
