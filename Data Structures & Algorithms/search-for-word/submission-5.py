class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        used = set()
        
        def dfs(i, j, wordIdx):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if (i, j) in used:
                return False

            c = board[i][j]
            if c == word[wordIdx]:
                wordIdx += 1
                used.add((i,j))

                if wordIdx == len(word):
                    return True
                
                if dfs(i+1, j, wordIdx) \
                    or dfs(i-1, j, wordIdx) \
                    or dfs(i, j+1, wordIdx) \
                    or dfs(i, j-1, wordIdx):
                    return True
                
                wordIdx -= 1
                used.remove((i, j))
                
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False