class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            delim = s.find('#', i)
            sz = int(s[i:delim])
            i = delim + 1
            ans.append(s[i:i+sz])
            i += sz
        return ans
