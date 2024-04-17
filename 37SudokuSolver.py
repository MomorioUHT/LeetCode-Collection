class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        def possiblePlace(y,x,n):
            for i in range(9):
                if str(board[y][i]) == n: return False
                elif str(board[i][x]) == n: return False
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(3):
                for j in range(3):
                    if str(board[y0+i][x0+j]) == n: return False
            return True

        def solve(board):
            for y in range(9):
                for x in range(9):
                    if board[y][x] == ".":
                        for n in range(1,10):
                            if possiblePlace(y,x,str(n)):
                                board[y][x] = str(n)
                                if solve(board): return True
                                board[y][x] = "."
                        return False
            return True
        solve(board)