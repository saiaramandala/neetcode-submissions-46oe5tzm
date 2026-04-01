class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(0, [], 0, target, candidates, res)
        return res

    def dfs(self, i, curSet, total, target, candidates, res):
        if total == target:
            res.append(curSet.copy())
            return

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            if  total + candidates[j] > target:
                break

            curSet.append(candidates[j])
            self.dfs(j + 1, curSet, total + candidates[j],target, candidates, res)
            curSet.pop()

    

        