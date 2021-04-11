# 输入
# "nowcoder. a am I"

# 返回值
# "I am a nowcoder."


# split()方法 指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串 返回分割后的字符串列表
# reverse() 函数用于反向列表中元素 
#  join()方法将序列中的元素以指定的字符连接生成一个新的字符串 
# str.join(sequence)
# sequence -- 要连接的元素序列

class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        l = s.split()
        if len(l) == 0:
            return s
        l.reverse()
        news = ' '.join(l)
        return news

# 自己编写split()函数功能
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        l = []
        tmp = ''
        for item in s:
            if item != ' ':
                tmp += item
            else:
                l.append(tmp)
                tmp = ''
        l.append(tmp)
#         l = s.split()
        if len(l) == 0:
            return s
        l = l[::-1]
        news = ' '.join(l)
        return news
