# 给你两个二进制字符串，返回它们的和（用二进制表示）。

# 输入为 非空 字符串且只包含数字 1 和 0。

# 把两个字符串改成相同长度，然后从最后一位往前计算，记录下进位即可
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n = len(a),len(b)
        if m>n:
            b = '0'*(m-n)+b
        elif m<n:
            a = '0'*(n-m)+a
        num = len(a)
        array = 0
        ans = ''
        for i in range(num-1,-1,-1):
            if a[i] == '1' and b[i] == '1':
                if array == 0:
                    ans = '0' + ans
                    array = 1
                else:
                    ans = '1' + ans
                    array = 1
            elif a[i] == '0' and b[i] == '0':
                if array == 0:
                    ans = '0' + ans
                else:
                    ans = '1' + ans
                    array = 0
            else:
                if array == 0:
                    ans = '1' + ans
                    array = 0
                else:
                    ans = '0' + ans
                    array = 1
        if array == 1:
            ans = '1' + ans
        return ans
