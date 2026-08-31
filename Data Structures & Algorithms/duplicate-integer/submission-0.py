class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        HashSet = set()

        for i in nums:
            if i in HashSet:
                return True
                
            HashSet.add(i)

        return False