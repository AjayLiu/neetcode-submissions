from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansDict = defaultdict(list) # maps from tuple to list
        for s in strs:
            # Count occurrences
            occ = [0] * 26
            for c in s:
                occ[ord(c) - ord('a')] += 1
            ansDict[tuple(occ)].append(s)
        
        return list(ansDict.values())