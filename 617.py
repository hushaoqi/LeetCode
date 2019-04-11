# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None: return t2
        if t2 is None:return t1
        t = TreeNode(t1.val + t2.val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        return t

    # 层序遍历
    def print_tree(self, root: TreeNode):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left is not None:
                queue.append(node.left)
            #else:print("null", end=' ')
            if node.right is not None:
                queue.append(node.right)
            #else:print("null", end=' ')



if __name__ == '__main__':
    s = Solution()
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)
    '''
    输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                   
    输出: 
    合并后的树:
             3
            / \
           4   5
          / \   \ 
         5   4   7
    '''
    res = s.mergeTrees(tree1, tree2)

    s.print_tree(res)

