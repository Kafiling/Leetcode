class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if not nums[i]==nums[i-1]:
                nums[k] = nums[i]
                k+=1
            i+=1
        if k == 0: k=1
        return k
