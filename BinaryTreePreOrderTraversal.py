class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode()) -> list[list[int]]:

    output = []
    q = [root]

    while q:
        l = len(q)
        temp = []
        for i in range(l):
            node = q.pop(0)
            if node:
                temp.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if temp:
            output.append(temp)
    return output

print(levelOrder([3,9,20,None, None,]))