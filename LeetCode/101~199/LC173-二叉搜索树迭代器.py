# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：

#     BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
#     boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
#     int next()将指针向右移动，然后返回指针处的数字。

# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。

# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def mid_order(node,arr):
            if not node:
                return None
            mid_order(node.left,arr)
            arr.append(node)
            mid_order(node.right,arr)
            return arr
        self.num = mid_order(root,[])
        minnum = self.num[0].val
        self.ptr = TreeNode(minnum-1)
        self.num.insert(0,self.ptr)
        self.flag = True
        self.index = 0
        self.len = len(self.num)


    def next(self) -> int:
        if self.flag:
            self.ptr = self.num[1]
            self.flag = False
            self.index = 1
            return self.ptr.val
        else:
            self.index += 1
            self.ptr = self.num[self.index]
            return self.ptr.val


    def hasNext(self) -> bool:
        if self.index < self.len-1:
            return True
        else:
            return False




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
