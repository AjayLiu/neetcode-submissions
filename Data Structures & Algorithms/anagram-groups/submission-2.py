from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counterDict = defaultdict(list)
        for s in strs:
            counter = tuple(sorted(list(Counter(s).items())))
            counterDict[counter].append(s)

        # print (counterDict.items())
        ans = [v for k, v in counterDict.items()]
        return ans



        
