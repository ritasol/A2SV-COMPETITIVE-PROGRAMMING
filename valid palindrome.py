class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for i in s:
            if i.isalpha() == True:
                i = i.lower()
        
        
    
        if s == s[::-1]:
            return True