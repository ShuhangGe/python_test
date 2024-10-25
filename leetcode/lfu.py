from collections import OrderedDict
from collections import defaultdict
class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.mincount = 0
        self.capacity = capacity
        self.cache = {}
        self.visited = {}
        #默认字典嵌套一个有序字典，外层字典的键是访问次数，有序字典会根据放入元素的先后顺序进行排序        self.key_list = defaultdict(OrderedDict)
 
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        #如果该key已经存在，修改value并且次数+1
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        
        #如果缓存满了，则删除最少访问次数
        if len(self.cache) == self.capacity:
            #找到最小访问次数
            temp_key, tmep_val = next(iter(self.key_list[self.mincount].items()))
                
            # min_visit = min(self.visited, key=lambda x: self.visited[x])
            del self.cache[temp_key]
            del self.visited[temp_key]
            del self.key_list[self.mincount][temp_key]
            
            self.cache[key] = value
            self.visited[key] = 0
        
        #添加时默认都是1，所以都放在访问次数为1的层中
        self.mincount = 1
        self.cache[key] = value
        self.visited[key] = 1
        #对记录字典进行赋值{1：{key:none, key1:none}}
        self.key_list[1][key] = None
 
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1
        
        #取出该key的访问次数
        count = self.visited[key]
        #对访问次数进行+1
        self.visited[key] += 1
        #对记录字典进行更新
        self.key_list[count].pop(key)
        self.key_list[count+1][key] = None
        
        #如果访问次数等于最小访问次数，并且该次数下已经没有值了，则最小访问次数+1，为下次加入做准备
        if count == self.mincount and len(self.key_list[count]) == 0:
            self.mincount += 1
        
        return self.cache[key]
        