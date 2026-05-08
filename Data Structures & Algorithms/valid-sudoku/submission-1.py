class Solution:
    def scanRow(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                b = board[i][j]
                if b != ".":
                    if b in seen:
                        return False
                    seen.add(b)
        return True
    
    def scanBox(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(9):
                    b = board[(i*3)+(k//3)][(j*3)+k%3]
                    if b != ".":
                        if b in seen:
                            return False
                        seen.add(b)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(self.scanRow(board))
        print(self.scanRow(list(zip(*board))))
        print(self.scanBox(board))
        return self.scanRow(board) and self.scanRow(list(zip(*board))) and self.scanBox(board)