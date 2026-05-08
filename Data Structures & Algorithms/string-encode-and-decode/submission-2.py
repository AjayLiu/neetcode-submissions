class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ";" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find(";", i)
            leng = int(s[i:j])
            decoded = s[j+1:j+leng+1]
            ans.append(decoded)
            i = j + leng + 1
        return ans
