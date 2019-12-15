class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.sz = 0
        self.k2lv = {}
        self.lv2k2v = {}

    def get(self, key: int) -> int:
        if key not in self.k2lv:
            return -1
        lv = self.k2lv[key]
        val = self.lv2k2v[lv][key]
        self._levelup(lv, key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap <= self.sz:
            self._evict(key, value)
            
        assert self.cap > self.sz
        self.sz += 1
        self.k2lv[key] = 0
        self.lv2k2v.setdefault(0, {})
        self.lv2k2v[0][key] = value
        
    def _levelup(self, lv, key, val):
        self.lv2k2v[lv].pop(key)
        # assert len(self.lv2kv[lv]) >= 0
        if len(self.lv2k2v[lv]) == 0:
            self.lv2k2v.pop(lv)
        self.lv2k2v.setdefault(lv+1, {})
        self.lv2k2v[lv+1][key] = val
        self.k2lv[key] += 1
    
    def _evict(self, key, value):
        for lv in range(987654321):
                if lv in self.lv2k2v:
                    break
        k,v = next(iter(self.lv2k2v[lv].items()))
        self.lv2k2v[lv].pop(k)
        if len(self.lv2k2v[lv]) == 0:
            self.lv2k2v.pop(lv)
        self.k2lv.pop(k)
        self.sz -= 1

        
'''
Misunderstood LFU as LRU, hence this bonus implementation...
LFU := Evict the least frequently used entry when the capacity is full
LRU := Evict the least recently used entry when the capacity is full
```
