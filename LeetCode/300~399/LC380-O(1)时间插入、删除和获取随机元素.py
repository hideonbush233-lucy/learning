# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

#     insert(val)：当元素 val 不存在时，向集合中插入该项。
#     remove(val)：元素 val 存在时，从集合中移除该项。
#     getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.length = 0



    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.stack:
            self.stack.append(val)
            self.length += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.stack:
            self.stack.remove(val)
            self.length -= 1
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        k = random.randint(0,self.length-1)
        return self.stack[k]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
