linkedLists = {}
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

def dfsPath(node, visited, visited_val, target):
    visited.append(node)
    visited_val.append(node.value)
    if node.value == target:
        return visited_val
    if node.left:
        dfsPath(node.left, visited, visited_val, target)
    if node.right:
        dfsPath(node.right, visited, visited_val, target)
    visited.pop()
    visited_val.pop()

def dfs(node, visited, visited_val, level) :
    visited.append(node)
    visited_val.append(node.value)
    if level in linkedLists:
        linkedLists[level].append(node.value)
    else:
        linkedLists[level] = [node.value]
    if node.left:
        if node.left not in visited:
            dfs(node.left, visited, visited_val, level + 1)
    if node.right:
        if node.right not in visited:
            dfs(node.right, visited, visited_val, level + 1)

def bfs(node):
    visited = []
    visited_val = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        visited.append(current)
        visited_val.append(current.value)
        if current.left:
            if current.left not in visited:
                queue.append(current.left)
        if current.right:
            if current.right not in visited:
                queue.append(current.right)
    print(visited_val)

def printInorder(node):
    if node:
        printInorder(node.left)
        print(node.value)
        printInorder(node.right)

def printPostorder(node):
    if node:
        printInorder(node.left)
        printInorder(node.right)
        print(node.value)

def printPreorder(node):
    if node:
        print(node.value)
        printInorder(node.left)
        printInorder(node.right)
root = Node(1)
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(7) 
root.right.right = Node(8) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.right.left = Node(6)
#print("Inorder: ")
#printInorder(root)
#print("Postorder: ")
#printPostorder(root)
#print("Preorder: ")
#printPreorder(root)
visited = []
visited_val = []
print(dfsPath(root, visited, visited_val, 6))
