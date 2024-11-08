class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = nums[0]
        for i in range(len(nums)-1):
            sum = max(sum+nums[i+1],nums[i+1])
            if sum > maxSum:
                maxSum=sum

        return maxSum
