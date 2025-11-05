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
    int maxDiameter = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
       getHeight(root);
       return maxDiameter; 
    }
 private:
    int getHeight(TreeNode* node){
        if(!node) return 0;
        int leftHeight = getHeight(node->left);
        if (leftHeight == -1) return -1;

        int rightHeight = getHeight(node->right);
        if (rightHeight == -1) return -1;
        maxDiameter = max(maxDiameter,leftHeight+rightHeight);

        return max(leftHeight, rightHeight) + 1 ;
    }
};