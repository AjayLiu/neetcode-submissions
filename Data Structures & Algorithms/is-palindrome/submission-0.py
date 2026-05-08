class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                clean_string += c
        
        return clean_string.upper() == (clean_string.upper())[::-1]