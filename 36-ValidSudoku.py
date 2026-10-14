class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        final = []

        def duplicateCheck(x: list):
            res = []
            for i in x: 
                if i not in res: res.append(i)
            if len(res) != len(x): final.append("False")
            else: final.append("True")

        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if i%3 == 0 and j%3 == 0:
                    array = []
                    for a in range(i,i+3):
                        for b in range(j,j+3):
                            if board[a][b] != '.':
                                array.append(board[a][b])
                    duplicateCheck(array)
                
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != '.': row.append(board[i][j])
                if board[j][i] != '.': col.append(board[j][i])
            duplicateCheck(row)
            duplicateCheck(col)

        if "False" in final: return False
        else: return True