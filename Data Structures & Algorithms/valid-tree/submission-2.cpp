class Solution {
public:
    bool hasCycle(int i, int parent, vector<vector<bool>> &adj, vector<bool> &visited){
        // cout << "EXPLORING " << i << endl;

        if (i < 0 || i >= adj.size()){
            return false;
        }
        if(visited[i]){
            return true;
        }


        visited[i] = true;
        for(int j = 0; j < adj[i].size(); j++){
            if(adj[i][j]){
                // cout << "CHECK NEIGHBOR " << j << " OFF PARENT " << i << endl;
                if(j == parent)
                    continue;
                if(hasCycle(j, i, adj, visited)){
                    return true;
                }
            }
        }
        return false;
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<bool>> adj (n, vector<bool>(n));
        for(vector<int> e : edges){
            if(e[0] == e[1])
                return false;
            adj[e[0]][e[1]] = true;
            adj[e[1]][e[0]] = true;
        }

        vector<bool> visited (n);

        bool hasNoCycle = !hasCycle(0, -1, adj, visited);

        return hasNoCycle && find(visited.begin(), visited.end(), false) == visited.end();
    }
};
