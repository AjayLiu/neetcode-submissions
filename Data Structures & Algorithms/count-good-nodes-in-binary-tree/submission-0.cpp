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
    int countGoodNodes(TreeNode* root, int biggestValUpstream){
        if(!root){
            return 0;
        }
        int num = root->val;
        if(num >= biggestValUpstream){
            return 1 + countGoodNodes(root->left, num) + countGoodNodes(root->right, num);
        }
        return countGoodNodes(root->left, biggestValUpstream) + countGoodNodes(root->right, biggestValUpstream);
    }

    int goodNodes(TreeNode* root) {
        return countGoodNodes(root, -101);
    }
};
