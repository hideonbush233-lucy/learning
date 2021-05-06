# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：

#     所有数字（包括目标数）都是正整数。
#     解集不能包含重复的组合。


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(idx,res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    if path not in ans:
                        ans.append(path[:])
                return

            for i in range(idx,len(candidates)):
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i+1,res+candidates[i])
                path.pop()
        candidates.sort()   
        if sum(candidates) < target:
            return []
        dfs(0,0)
        return ans
