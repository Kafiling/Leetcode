class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        mag = {}
        for i in magazine:
            ransom[i] = 1 + ransom.get(i,0)
        for i in ransomNote:
            print(i,ransom)
            if i not in ransom or ransom[i] <= 0:
                return False
            ransom[i] -= 1
        return True
