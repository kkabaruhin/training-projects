
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from queue import Queue
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (root == None): return None
        if (root.left == None): return root
        q = Queue(maxsize = 4096)
        newQ = Queue(maxsize = 4096)
        q.put(root.right)
        prevNode = root.left
        while (q.empty() == False):
            currNode = q.get()
            prevNode.next = currNode
            if prevNode.left != None:
                newQ.put(prevNode.left)
                newQ.put(prevNode.right)
            if (q.empty()):
                if (currNode.left != None):
                    newQ.put(currNode.left)
                    newQ.put(currNode.right)
                q = newQ
                if (q.empty()): break
                newQ = Queue(maxsize = 4096)
                currNode = q.get()
            prevNode = currNode
        return root
node4 = Node(4)
node5 = Node(5)
node2 = Node(2, node4, node5)
node7 = Node(7)
node3 = Node(3, None, node7)
root = Node(1, node2, node3)
sol = Solution()
print(sol.connect(root))