class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [],[]
        
        def combination(i, target):
            if i >= len(nums):
                if target == 0 :
                    res.append(sol[:])
                return

            #pick
            if nums[i] <= target:
                sol.append(nums[i])
                combination(i , target - nums[i] )

                sol.pop()

            combination(i+1 , target)

        combination(0,target)
        return res 