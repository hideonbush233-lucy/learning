# 给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。
# 设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.stack = []
        # self.iteration = iterator
        while iterator.hasNext():
            self.stack.append(iterator.next())
        self.length = len(self.stack)
        self.index = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.stack[self.index]


        

    def next(self):
        """
        :rtype: int
        """
        val = self.stack[self.index]
        self.index += 1
        return val
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.length > self.index
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
