# 给定一个二叉树

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        que = [root]
        nextlevel = []
        while que:
            n = len(que)
            for i in range(n-1):
                que[i].next = que[i+1]
                if que[i].left:
                    nextlevel.append(que[i].left)
                if que[i].right:
                    nextlevel.append(que[i].right)
            if que[-1].left:
                nextlevel.append(que[-1].left)
            if que[-1].right:
                nextlevel.append(que[-1].right)
            que = nextlevel[:]
            nextlevel = []
        return root
