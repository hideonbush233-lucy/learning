# 你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

#     你写出一个秘密数字，并请朋友猜这个数字是多少。
#     朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
#     朋友根据提示继续猜，直到猜出秘密数字。

# 请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。

#     xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
#     yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。

# 请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # n = len(secret)
        # x = 0
        # y = 0
        # used = [False]*n
        # for i in range(n):
        #     if secret[i] == guess[i]:
        #         x += 1
        #         if used[i]:
        #             if secret[i] in guess[i+1:]:
        #                 new_guess = guess[i+1:]
        #                 for m in range(len(guess[i+1:])):
        #                     if secret[i] == new_guess[m]:
        #                         used[i+m+1] = True
        #             else:
        #                 y -= 1
        #         used[i] = True
        #     else:
        #         if secret[i] in guess:
        #             for j in range(n):
        #                 if guess[j] == secret[i] and not used[j]:
        #                     used[j] = True
        #                     y += 1
        #                     break
        # return str(x)+'A'+str(y)+'B'

        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
        base = set(guess)
        for v in base:
            if v in secret:
                b += min(guess.count(v),secret.count(v))
        b = b-a
        return(str(a)+"A"+str(b)+"B")
