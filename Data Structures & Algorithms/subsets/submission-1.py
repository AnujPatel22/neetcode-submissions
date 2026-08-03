class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res,sol = [],[]

        def sub(i):
            #base case
            if i >= len(nums):
                res.append(sol[:])
                return
            
            #pick
            sol.append(nums[i])
            sub(i+1)

            #backtrack
            sol.pop()

            #notpick
            sub(i+1)

        sub(0)
        return res


