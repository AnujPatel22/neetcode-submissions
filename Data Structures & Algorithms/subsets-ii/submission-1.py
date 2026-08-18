class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def subfun(i,sol):
            if i == len(nums):
                res.append(sol[:])
                return

            #pick
            sol.append(nums[i])
            subfun(i+1 ,sol)

            sol.pop()

            #not pick
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            subfun(i+1, sol)

        subfun(0, [])
        return res
        