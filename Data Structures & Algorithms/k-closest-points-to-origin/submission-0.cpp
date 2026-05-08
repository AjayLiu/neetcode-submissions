class Solution {
public:

    struct Point {
        int x, y;
        Point(int x, int y){
            this->x = x;
            this->y = y;
        }

        bool operator < (const Point &other) const {
            return x*x + y*y > other.x * other.x + other.y * other.y;
        }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<Point> pq;
        for(vector<int> coord : points){
            pq.push(Point(coord[0], coord[1]));
        }

        vector<vector<int>> ans;
        
        while(k--){
            vector<int> coord;
            Point closestPoint = pq.top();
            pq.pop();
            coord.push_back(closestPoint.x);
            coord.push_back(closestPoint.y);

            ans.push_back(coord);
        }

        return ans;
    }
};
