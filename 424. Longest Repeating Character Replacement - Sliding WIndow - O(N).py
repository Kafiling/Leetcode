class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # it basically Longest Repeating Character that allow error up to k
        l=0
        hash = {}
        res=0

        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r],0)

            # check condition (allow other char upto k)
            # windowsize - mostFrequentChar(doesnt need to be replace) >= k -> shrink window
            while (r-l+1) - max(hash.values()) > k :
                hash[s[l]] -= 1
                l+=1
            
            res = max(res,r-l+1) 
        return res

# This solution's time complexity is O(26N) 

        
