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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        map<int,int> inMap;
        for(int i =0; i< inorder.size();i++){
            inMap[inorder[i]] = i;
        }
        int postorderIndex = postorder.size()-1;
        return build(postorder, inMap, postorderIndex, 0, inorder.size()-1);
    }

     TreeNode* build (vector<int>& postorder, map<int,int>& inMap, int& postorderIndex,int inorderStart, int inorderEnd ){
                            
        if(inorderStart>inorderEnd) return NULL;

        int rootVal = postorder[postorderIndex--];
        TreeNode* root = new TreeNode(rootVal);

        int inorderIndex = inMap[rootVal];

        root->right = build(postorder, inMap, postorderIndex, inorderIndex+1, inorderEnd);

        root->left = build(postorder, inMap, postorderIndex,inorderStart, inorderIndex-1);

        return root;

    }
};