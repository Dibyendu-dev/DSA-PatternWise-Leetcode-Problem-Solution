/*The Node structure is defined as
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/

// return the Kth largest element in the given BST rooted at 'root'
class Solution {
  public:
     int count = 0;
    int result = 0;
    int kthLargest(Node *root, int k) {
        // Your code here
        reverseInorder(root, k);
        return result;
    }
    
    void reverseInorder(Node* node, int k) {
        if (!node) return;  
        reverseInorder(node->right, k);
        count++;
        if (count == k) {
            result = node->data;
            return;
        }
        reverseInorder(node->left, k);
    }
};