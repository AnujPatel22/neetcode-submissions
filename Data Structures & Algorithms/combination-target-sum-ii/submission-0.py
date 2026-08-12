class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        candidates.sort()

        def comsum(i, target):
            if target == 0:
                res.append(sol[:])
                return
            
            for j in range(i, len(candidates)):
                if target < candidates[j] :
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                sol.append(candidates[j])
                comsum(j+1, target - candidates[j])
                sol.pop()
                
                
        comsum(0, target)
        return res

