class Solution {
public:

    bool dfs(vector<vector<int>> &adj, vector<bool> &visited, vector<bool> &seen, int i, vector<int>& topSort){
        if(seen[i]){
            return false;
        }
        if(visited[i]){
            return true;
        }

        visited[i] = true;
        seen[i] = true;
        for(int neighbor : adj[i]){
            bool ans = dfs(adj, visited, seen, neighbor, topSort);
            if(!ans)
                return false;
        }
        seen[i] = false;
        topSort.push_back(i);
        return true;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for(vector<int> v : prerequisites){
            adj[v[0]].push_back(v[1]);
        }
        
        vector<bool> visited(numCourses);
        vector<int> topSort;

        for(int i = 0; i < numCourses; i++){
            vector<bool> seen(numCourses);
            if(!dfs(adj, visited, seen, i, topSort))
                return {};
        }
        return topSort; 
    }
};
