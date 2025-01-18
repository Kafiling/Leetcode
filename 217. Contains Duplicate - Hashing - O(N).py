class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for i in nums:
            if i in memo:
                return True
            memo.add(i)
        return False
        
