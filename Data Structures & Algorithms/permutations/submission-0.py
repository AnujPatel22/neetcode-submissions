class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def perm(sol):
            if len(nums) == len(sol):
                res.append(sol[:])
                return

            for i in nums:
                if i not in sol:

                    sol.append(i)
                    perm(sol)

                    sol.pop()

        perm([])
        return res