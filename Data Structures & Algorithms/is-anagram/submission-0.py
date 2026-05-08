class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {} # Maps {character : number of appearance}
        dictT = {}
        for char in s:
            dictS[char] = dictS.get(char, 0) + 1
        
        for char in t:
            dictT[char] = dictT.get(char, 0) + 1

        return dictS == dictT