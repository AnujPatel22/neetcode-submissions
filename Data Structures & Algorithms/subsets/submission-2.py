class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        
        def subset(i):
            if i >= len(nums):
                res.append(sol[:])
                return


            sol.append(nums[i])
            subset(i+1)

            sol.pop()

            subset(i+1)

        subset(0)
        return res