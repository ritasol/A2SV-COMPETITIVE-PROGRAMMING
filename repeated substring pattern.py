class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # a = "ab"
        # print(s.count(a))
        string = ""
        for i in s:
            string += i
            a = string
            if s.count(a) != 1 and (s.count(a) * len(string)) == n:
                return True
        return False
