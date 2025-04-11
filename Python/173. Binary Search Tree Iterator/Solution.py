
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


from collections import deque


class BSTIterator:
    def __init__(self, root):
        fakeRoot = TreeNode(-1, root, None)
        self.path = deque()
        self.len = 0
        self.findMinAndAddToPath(fakeRoot)

    def findMinAndAddToPath(self, root1):
        root = root1
        while (root != None):
            self.path.append(root)
            self.len += 1
            root = root.left

    def next(self) -> int:
        answer = self.path.pop()
        self.len = self.len - 1
        currNode = answer
        if currNode.right != None:
            self.findMinAndAddToPath(currNode.right)
        else:
            prevNode = currNode
            currNode = self.path.pop()
            self.len = self.len - 1
            while self.len > 0 and currNode.right == prevNode:
                prevNode = currNode
                currNode = self.path.pop()
                self.len = self.len - 1
            if (self.len != 0):
                self.path.append(currNode)
                self.len += 1
        return answer.val

    def hasNext(self) -> bool:
        return self.len != 0

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15, n9, n20)
n7 = TreeNode(7, n3, n15)
x = BSTIterator(n7)
print(x.next())
print(x.next())
print(x.hasNext())
print(x.next())
print(x.hasNext())
print(x.next())
print(x.hasNext())
print(x.next())
print(x.hasNext())