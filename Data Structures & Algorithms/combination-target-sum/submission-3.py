class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [],[]
        

        def combination(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or i == len(nums) :
                return

            #Pick 
         
            sol.append(nums[i])
            combination(i, cur_sum + nums[i])

            sol.pop()

            combination(i+1 , cur_sum)

        combination(0,0)
        
        return res 