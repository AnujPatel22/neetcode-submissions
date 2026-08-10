class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        initial, final = [], []

        def comsum(i, target):
            if i >= len(nums):
                if target == 0:
                    final.append(initial[:])
                return

            if nums[i] <= target :
                initial.append(nums[i])
                comsum(i, target - nums[i])

                initial.pop()

            comsum(i+1, target)

        comsum(0, target)
        return final    
