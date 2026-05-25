class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(run:str, opens: int, closes: int):
            if closes > opens or opens > n:
                return

            if closes == n:
                ans.append(run)
            
            dfs(run + "(", opens + 1, closes)
            dfs(run + ")", opens, closes + 1)
        
        dfs("", 0, 0)
        return ans
                 
