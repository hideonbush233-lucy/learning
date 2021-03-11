# 借助一个辅助栈，比较二者，如果不同，说明pushV压入栈中未弹出，接着pushV后移继续比较，如果相同说明这一个值压入了就立即弹出了
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        res = []
        for i in popV:
            if res and res[-1] == i:
                res.pop()
                continue
            elif pushV:
                while pushV and pushV[0] != i:
                    res.append(pushV.pop(0))
                if pushV and pushV[0] == i:
                    pushV.pop(0)
                    continue
                if not pushV:
                    return False
            else:
                return False
        return True
