# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
# 请对此链表进行深拷贝，并返回拷贝后的头结点。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# 多次遍历，暴力破解
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        cur = pHead
        res = []
        random = [] 
        while cur:   # 遍历原链表，把数据点和random点记录下来
            res.append(cur.label)
            if cur.random:
                random.append(cur.random.label)
            else:
                random.append(None)
            cur = cur.next
        
        p = RandomListNode(res[0])
        cur = p
        for i in range(1,len(res)):  # 遍历建立主结点，不管随机结点
            cur.next = RandomListNode(res[i])
            cur = cur.next
        
        cur = p
        j = 0
        while cur:  # 双循环，检索随机结点
            new_cur = p
            if random[j] == None:
                cur.random = None
            else:
                while new_cur:
                    if new_cur.label == random[j]:
                        cur.random = new_cur
                        break
                    new_cur = new_cur.next
            cur = cur.next
            j += 1
        return p
