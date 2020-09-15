class LRUCache:

    def __init__(self, capacity: int):
        self.keys = []
        self.values = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        try:
            idx = self.keys.index(key)
            self.keys = self.keys[:idx] + self.keys[idx+1:] + [self.keys[idx]]
            self.values = self.values[:idx] + self.values[idx+1:] + [self.values[idx]]
            return self.values[-1]
        except:
            return -1
        
    def put(self, key: int, value: int) -> None:
        try:
            idx = self.keys.index(key)
            self.values[idx] = value
            self.keys = self.keys[:idx] + self.keys[idx+1:] + [self.keys[idx]]
            self.values = self.values[:idx] + self.values[idx+1:] + [self.values[idx]]
        except:
            self.keys.append(key)
            self.values.append(value)
            if len(self.keys) > self.capacity:
                self.keys.pop(0)
                self.values.pop(0)

#Faster way using ordered dict
class LRUCache:

    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if len(self.dic) == self.capacity:
                self.dic.popitem(last=False) 
                
        self.dic[key] = value