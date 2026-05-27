class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def dfs(s, opens, closes):
            if opens > n or closes > n:
                return
            if closes > opens:
                return
            if opens == closes == n:
                ans.append(s)
            
            dfs(s + "(", opens + 1, closes)
            dfs(s + ")", opens, closes + 1)
        dfs("", 0,0)
        return ans