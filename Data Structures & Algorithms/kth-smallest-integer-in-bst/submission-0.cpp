/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    int inorder(TreeNode* node, int &rank, int k){
        if(!node){
            return -1;
        }
        cout << "RANK " << rank << " at NODE " << node->val << endl;

        
        int leftTree = inorder(node->left, rank, k);
        if(leftTree != -1){
            return leftTree;
        }

        if(rank == k){
            return node->val;    
        }
        rank++;
        
        int rightTree = inorder(node->right, rank, k);
        if(rightTree != -1){
            return rightTree;
        }

        return -1;
    }
    int kthSmallest(TreeNode* root, int k) {
        int rank = 1;
        return inorder(root, rank, k);
    }
};
