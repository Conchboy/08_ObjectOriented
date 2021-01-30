class Cat:
    def __init__(self, name):
        self.name = name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)


# tom是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del关键字可以删除一个对象

print("*_* " * 50)
del tom
