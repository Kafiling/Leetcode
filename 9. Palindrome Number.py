class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return checkPalindrome(str(x))
def checkPalindrome(string):
        if len(string) < 1:
            return True
        return string[0] == string[len(string)-1] and checkPalindrome(string[1:len(string)-1])
