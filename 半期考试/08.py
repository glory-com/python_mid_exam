# 题目H：采用面向对象方法实现列表元素计数
# 实现父类Counting类的counting()方法，该方法实现对输入一维列表(皆为整数或浮点数)的元素进行重复计数，并存于字典中。该字典的key为列表中某一元素，value为元素出现次数。

# 在实现父类后，继承该父类并实现子类CountingMore，实现子类的counting_maxkey()方法，返回已构建字典中最大键值元素对应的重复次数。


class Counting(object):

    def __init__(self, input_data):
        self.data = input_data#初始话属性

    def counting(self):
        dict = {}
        #枚举元素，记录出现次数
        for i in self.data :
            if i not in dict :
                dict[i] = 1 
            else:
                dict[i] += 1 

        return dict 
        
class CountingMore(Counting):

    def __init__(self, input_data):
        super().__init__(input_data)

    def counting_maxkey(self):
        #调用方法，实例化dict
        dict = self.counting()
        #找到最大值
        max_key = max(dict)
        return dict[max_key]


def counting_list(data):

    countingObject    = CountingMore(data)        # CountingMore类实例化
    all_key_counting = countingObject.counting()  # 调用子类继承自父类的方法counting()
    max_key = countingObject.counting_maxkey()    # 调用子类的方法counting_maxkey()

    return [all_key_counting, max_key]
