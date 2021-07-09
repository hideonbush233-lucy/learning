# 给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。

# 列表中的每个元素只可能是整数或整数嵌套列表

# 提示：你可以假定这些字符串都是格式良好的：

#     字符串非空
#     字符串不包含空格
#     字符串只包含数字0-9、[、-、,、]


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def dfs(elem):
            if type(elem) == int:
                return NestedInteger(elem)
            li = NestedInteger()  # 这个对象为空时是一个空列表
            for i in elem:
                li.add(dfs(i))
            return li

        return dfs(eval(s))
