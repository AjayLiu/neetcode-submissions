from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            freq = tuple(sorted(Counter(s).items()))
            ans[freq].append(s)
        return list(ans.values())