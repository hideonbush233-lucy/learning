# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

# 该方法采用c++编写没有问题，Python不知道为什么不行 （python没有无符号右移操作，所以需要越界检查一波！！！！！）
# 三位加法：

#     101 ^ 111 = 0010 （没有处理进位的加法）
#     (101 & 111) << 1 = 101 << 1 = 1010 （此处得到哪一位需要加上进位，为1的地方表示有进位需要加上）

#     0010 ^ 1010 = 1000 （没有处理进位的加法 + 进位 = 没有处理进位的加法）

#     (0010 & 1010) << 1 = 0010 << 1 = 00100 （查看是否有新的进位需要处理）

#     1000 ^ 00100 （没有处理进位的加法 + 进位 = 没有处理进位的加法）

#     (1000 & 00100) << 1 = 00000 << 1 = 000000 (进位为0，所以没有要处理的进位了)

# 更高位加法：依上边类推
# class Solution {
# public:
#     int Add(int num1, int num2) {
#         int res = num1^num2;
#         int carry = (num1&num2)<<1;
#         num1 = res;
#         num2 = carry;
#         while(num2!=0){
#             res = num1^num2;
#             carry = (num1&num2)<<1;
#             num1 = res;
#             num2 = carry;
#         }
#         return res;
#     }
# };

# python方法
class Solution:
    def Add(self, num1, num2):
        # write code here
        while(num2): 
           num1, num2 = (num1^num2) & 0xFFFFFFFF,((num1&num2)<<1) & 0xFFFFFFFF
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)
