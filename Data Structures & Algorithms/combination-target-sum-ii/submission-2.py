class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comsum(i,curr_sum, sol):
            if curr_sum == 0:
                res.append(sol[:])
                return

            for j in range(i, len(candidates)):
                if curr_sum < candidates[j]:
                    break

                if j>i and candidates[j] == candidates[j-1]:
                    continue

                sol.append(candidates[j])
                comsum(j+1, curr_sum - candidates[j], sol)

                sol.pop()
            
        comsum(0, target, [])
        return res