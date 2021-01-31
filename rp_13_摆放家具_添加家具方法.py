class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python 能够自动将一对括号内部的代码连接在一起
        return ("户型： %s\n总面积：%.2f (剩余面积： %s) \n家具列表： %s"
                % (self.house_type, self.area,
                   self.free_area, self. item_list))

    def add_item(self, item):
        # 1.判断家具的面积是否超过剩余面积
        if item.area > self.free_area:
            print("%s的占地太大, 实在放不下啊!" % item.name)
            return
        # 2. 将家具添加到房子中
        print("要添加 %s" % item)
        # 计算房子的剩余面积
        self.free_area -= item.area
        # 在房子的家具列表中加入当前添加的家具
        self.item_list.append(item.name)


# 1. 创建家具
bed = HouseItem("席梦思", 40)
wardrobe = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 8)

print(bed)
print(wardrobe)
print(table)

# 创建房子对象
my_house = House("两室一厅", 90)

# 添加家具
my_house.add_item(bed)
my_house.add_item(wardrobe)
my_house.add_item(wardrobe)
my_house.add_item(table)

print(my_house)
