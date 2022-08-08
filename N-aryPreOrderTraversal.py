class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder(root: 'Node') -> list[int]:

    if root is None:
        return None

    output = []
    search(root, output)
    return output

def search(curr, output):
    if curr is None:
        return
    
    output.append(curr.val)

    for i in output:
        search(i, output)


print([1,None,3,2,4,None, 5,6])