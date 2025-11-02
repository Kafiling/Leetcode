class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Using Sliding window to solve

        hashmap = {}

        # Right ++ til end of arr
        for right in range(len(nums)):
            # add right into hashmap
            if nums[right] in hashmap:
                return True # found same number
            else : 
                hashmap[nums[right]] = 1
            
            #move left-sided window
            if right - k >= 0 :
                hashmap.pop(nums[right-k])

        return False
        
