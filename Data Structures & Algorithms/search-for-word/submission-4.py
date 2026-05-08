class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board: List[List[str]], word: str, i: int, j: int, visited: List[List[bool]]) -> bool:
            if word == "":
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if visited[i][j]:
                return False
            
            letter = board[i][j]
            print(visited)
            print("At",letter,"looking for",word[0])

            if(word[0] == letter):
                visited[i][j] = True
                up = dfs(board, word[1:], i-1, j, visited) 
                down = dfs(board, word[1:], i+1, j, visited) 
                left = dfs(board, word[1:], i, j-1, visited) 
                right = dfs(board, word[1:], i, j+1, visited) 
                visited[i][j] = False
                return up or down or left or right
            
            return False


        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                visited = [[False for _ in r] for r in board]
                if(dfs(board, word, i, j, visited)):
                    return True

        return False