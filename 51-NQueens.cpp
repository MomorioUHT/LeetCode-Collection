class Solution {
private:
    void solve(int row, int n, 
    vector<bool> &Vertical,
    vector<bool> &LeftDiagonal,
    vector<bool> &RightDiagonal,
    vector<string> &board,
    vector<vector<string>> &solutions) {
        if (row == n) {
            solutions.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            int ldv = row - col + (n - 1);
            int rdv = row + col;
            if (!Vertical[col] && !LeftDiagonal[ldv] && !RightDiagonal[rdv]) {
                board[row][col] = 'Q';
                // Claims
                Vertical[col] = true;
                LeftDiagonal[ldv] = true;
                RightDiagonal[rdv] = true;

                solve(row + 1, n, Vertical, LeftDiagonal, RightDiagonal, board, solutions);

                board[row][col] = '.';
                Vertical[col] = false;
                LeftDiagonal[ldv] = false;
                RightDiagonal[rdv] = false;
            }
        }
    }
public:
vector<vector<string>> solveNQueens(int n) {
        vector<bool> Vertical(n, false);
        vector<bool> LeftDiagonal((2 * n) - 1, false);
        vector<bool> RightDiagonal((2 * n) - 1, false);

        vector<vector<string>> solutions;
        vector<string> board(n, string(n, '.'));

        solve(0, n, Vertical, LeftDiagonal, RightDiagonal, board, solutions);

        return solutions;
    }
};