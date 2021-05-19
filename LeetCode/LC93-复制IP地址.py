# 给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。


# 回溯，确定结果index和ip开始的位置
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        segments = [0]*4
        def dfs(index,start):
            if index == 4:
                if start == len(s):
                    ip = ".".join(str(seg) for seg in segments)
                    ans.append(ip)
                return 
            if start == len(s):
                return 
            if s[start] == '0':
                segments[index] = 0
                dfs(index+1,start+1)
            addr = 0
            for end in range(start,len(s)):
                addr = addr*10+(ord(s[end])-ord('0'))
                if 0 < addr <= 255:
                    segments[index] = addr
                    dfs(index+1,end+1)
                else:
                    break

        dfs(0,0)
        return ans
