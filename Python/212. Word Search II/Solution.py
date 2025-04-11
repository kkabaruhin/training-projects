class Node:
    def __init__(self):
        self.contains = False
        self.nexts = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        currNode = self.root
        for c in word:
            if c not in currNode.nexts:
                currNode.nexts[c] = Node()
            currNode = currNode.nexts[c]

        currNode.contains = True


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        n = len(board)
        m = len(board[0])
        visit = []
        for i in range(n):
            visit.append([])
            for j in range(m):
                visit[i].append(False)
        answer = set()
        for i in range(n):
            for j in range(m):
                self.recursiveSearch(trie.root, answer, board, visit, i, j, '')
        return list(answer)

    def recursiveSearch(self, node, answer, board, visit, i, j, word):
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or visit[i][j]:
            return
        if board[i][j] not in node.nexts:
            return
        word = word + board[i][j]
        if node.nexts[board[i][j]].contains:
            answer.add(word)
        visit[i][j] = True
        self.recursiveSearch(node.nexts[board[i][j]], answer, board, visit, i + 1, j, word)
        self.recursiveSearch(node.nexts[board[i][j]], answer, board, visit, i - 1, j, word)
        self.recursiveSearch(node.nexts[board[i][j]], answer, board, visit, i, j + 1, word)
        self.recursiveSearch(node.nexts[board[i][j]], answer, board, visit, i, j - 1, word)

        visit[i][j] = False

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))