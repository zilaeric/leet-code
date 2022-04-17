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
    TreeNode* new_root; // root of new tree
    TreeNode* cur_node; // last node of new tree
    
    TreeNode* increasingBST(TreeNode* root) {
        new_root = new TreeNode(); // inititate new tree
        cur_node = new_root; // set last node to root
            
        inOrder(root); // traverse tree in order
            
        return(new_root->right);
    }
    
    // in order traversal
    void inOrder(TreeNode* root) {
        if (root == NULL) return;
        
        inOrder(root->left);
        
        cur_node->right = root; // add node to new tree
        root->left = NULL; // remove left child
        cur_node = cur_node->right; // update last node of new tree
        
        inOrder(root->right);
    }
};

