class Solution {
public:
    void dfs(vector<vector<char>> &board, int i, int j){
        if(i < 0 || j < 0 || i >= board.size() || j >= board[i].size()){
            return;
        }

        char &here = board[i][j];
        if(here == 'O'){
            here = 'B';
            dfs(board, i+1, j);
            dfs(board, i-1, j);
            dfs(board, i, j+1);
            dfs(board, i, j-1);
        }
    }

    void solve(vector<vector<char>>& board) {

        // Mark all border accessible O's into B
        for(int i = 0; i < board.size(); i++){
            // left border
            dfs(board, i, 0);

            // right border
            dfs(board, i, board[i].size()-1);
        }
        for(int j = 0; j < board[0].size(); j++){
            // top border
            dfs(board, 0, j);

            // bottom border
            dfs(board, board.size()-1, j);
        }

        // Mark all O's into X (since they weren't discovered by border DFS)
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if(board[i][j] == 'B'){
                    board[i][j] = 'O';
                }
            }
        }
    }
};
