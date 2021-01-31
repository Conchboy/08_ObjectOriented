class Women:
    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部可以访问对象的私有属性
        print("%s的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性在外部不能直接访问, 但是可以使用伪私有属性的访问方法
print(xiaofang._Women__age)
# 私有方法同样不能在方法外部调用, 但是也可以使用_women__secret()来访问
xiaofang._Women__secret()
