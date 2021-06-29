# 编写一段程序来查找第 n 个超级丑数。

# 超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [1]
        k = len(primes)
        i_index = [0] * k
        for i in range(1, n):
            ugly = min([primes[j] * nums[i_index[j]] for j in range(k)])
            nums.append(ugly)
            for j in range(k):
                if ugly == primes[j] * nums[i_index[j]]:
                    i_index[j] += 1
                
        return nums[n - 1]
