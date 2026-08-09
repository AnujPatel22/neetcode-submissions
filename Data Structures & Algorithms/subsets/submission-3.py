class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, final = [], []

        def sub(i):

            if i >= len(nums):
                final.append(curr[:])
                return

            curr.append(nums[i])
            sub(i+1)

            curr.pop()

            sub(i+1)

        sub(0)
        return final