# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            i = low + (high-low)//2
            if isBadVersion(i):
                high = i-1
            else:
                low = i+1
        return int(low)

            

        
            

