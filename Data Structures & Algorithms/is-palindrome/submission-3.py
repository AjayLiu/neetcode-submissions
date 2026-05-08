class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join([c.lower() if (c.isalnum()) else '' for c in s])
        print(clean)
        return clean == clean[::-1]