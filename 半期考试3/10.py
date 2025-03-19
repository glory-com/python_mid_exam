# 题目：采用面向对象方法实现车辆管理：
# 有一个父类 Auto，具有属性 brand 和 color，即汽车的品牌与颜色

# 有两个子类：Car 和 Bus。它们继承自 Auto 类。其中，Car 类表示轿车，Bus类表示大巴车。Bus类具备一个额外的私有属性carry_passengers, 即载客人数。

# 现在，有一个 AutoMarket 类，管理所有汽车的实例。该类具有以下方法：

# buy_auto(auto:Auto)：将一个汽车实例添加到汽车市场中。
# current_auto_storage()：显示所有添加到汽车市场中的汽车品牌、颜色、载客人数等属性。
# 要求：

# 请你填写如下 Python 代码，采用面向对象方法，使其能够顺利运行，满足上述要求。


class Auto(object):
    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

class Car(Auto): # 补全该类
    def __init__(self , brand , color) :
        super(Car , self).__init__(brand , color)

        

class Bus(Auto): 
    def __init__(self, brand, color, carry_passengers): # 补全该函数，需采用父类构造函数
        super(Bus , self).__init__(brand , color)
        self.carry_passengers = carry_passengers 
        
        
class AutoMarket(object):
    def __init__(self):
        self.auto = {'Car':[], 'Bus':[]}

    def buy_auto(self, auto):  # 补全该函数
        auto_class = auto.__class__.__name__
        self.auto[auto_class].append(auto)


    def current_auto_storage(self):   # 补全该函数
        for car in self.auto['Car']:
            print("Having car {0}, color is {1}".format(car._Auto__brand, car._Auto__color))
        for bus in self.auto['Bus']:
            print("Having bus {0}, color is {1}, carry_passengers is {2}".format(bus._Auto__brand, bus._Auto__color , bus.carry_passengers))


            
def testing_AutoMarket(auto_list):
    # 用于测试，此函数禁止操作，否则记为0分！
    auto_market = AutoMarket()
    for auto in auto_list:
        auto_type = auto[0].split("_")
        if auto_type[0] == "car":
            car = Car(brand = auto[1]['brand'],
                      color = auto[1]['color'])
            auto_market.buy_auto(car)
        elif auto_type[0] == "bus":
            bus = Bus(brand = auto[1]['brand'],
                      color = auto[1]['color'],
                      carry_passengers = auto[1]['carry_passengers']
                     )
            auto_market.buy_auto(bus)
        else:
            print("Incorrect auto type!")
    auto_market.current_auto_storage()


auto_list = [['car_1',{'brand':'audi_A4', 'color':'red'}],
             ['car_2',{'brand':'xiaomi_su7', 'color':'blue'}],
             ['bus_1',{'brand':'Jinlong', 'color':'write', 'carry_passengers':40}],
             ['car_3',{'brand':'byd_qin','color':'black'}]]

testing_AutoMarket(auto_list)


# Having car audi_A4, color is red
# Having car xiaomi_su7, color is blue
# Having car byd_qin, color is black
# Having bus Jinlong, color is write, carry_passengers is 40