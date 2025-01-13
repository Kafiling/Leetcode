class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter ="".join(ch for ch in s if ch.isalnum())
        s2 = filter.lower()
        i = 0
        j = len(s2)-1
        while i < j:
            if s2[i] != s2[j]:
                return False
            i +=1
            j -=1
        return True
