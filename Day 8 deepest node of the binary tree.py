from collections import deque
# A Python3 program to find value of the 
# deepest node in a given binary tree by method 3 
class new_Node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def deepestNode(root):
    if root==None:
        return 0
    q=deque()
    q.append(root)
    node=None
    while len(q)!=0:
        node=q.popleft()
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return node.data
 
# Driver Code
if __name__ == '__main__':
 
    root = new_Node(1) 
    root.left = new_Node(2) 
    root.right = new_Node(3) 
    root.left.left = new_Node(4) 
    root.right.left = new_Node(5) 
    root.right.right = new_Node(6) 
    root.right.left.right = new_Node(7) 
    root.right.right.right = new_Node(8) 
    root.right.left.right.left = new_Node(9) 
     
    # Calculating height of tree 
    levels = deepestNode(root) 
     
    # Printing the deepest node 
    print(levels)
#This code is contributed by Aprajita Chhawi 
