# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。

# 实现 LRUCache 类：

#     LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
#     int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#     void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？


class LRUCache:

    def __init__(self, capacity: int):
        self.lis = {}
        self.length = 0
        self.maxlen = capacity
        self.order = []

    def get(self, key: int) -> int:
        if key in self.lis:
            self.order.remove(key)
            self.order.append(key)
            return self.lis[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lis:
            self.lis[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if self.length < self.maxlen:
                self.lis[key] = value
                self.order.append(key)
                self.length += 1
            else:
                oldkey = self.order.pop(0)
                self.lis.pop(oldkey)
                self.lis[key] = value
                self.order.append(key)
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
