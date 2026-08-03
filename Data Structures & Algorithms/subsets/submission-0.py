class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol = [],[]

        def sub(i):
            if i >= len(nums):
                res.append(sol[:])
                return

            #Take 
            sol.append(nums[i])
            sub(i+1)

            #backtrack
            sol.pop()

            #Not take
            sub(i+1)

        sub(0)
        return res