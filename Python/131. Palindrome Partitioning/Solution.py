class Solution:
    answer = []
    def isPalindrom(self, str1):
        for i in range(len(str1) // 2):
            if (str1[i] != str1[len(str1) - 1 - i]):
                return False
        return True
    def distinct(self):
        i = 0
        while (i < len(self.answer)):
            j = i + 1
            while (j < len(self.answer)):
                if self.answer[i] == self.answer[j]:
                    del self.answer[j]
                else:
                    j += 1
            i += 1
    def dfs(self, prev, start):
        self.answer.append(prev.copy())
        for i in range(start, len(prev) - 1):
            if (i > 0):
                if (len(prev[i - 1]) == 1 and len(prev[i + 1]) == 1 and prev[i-1][0] == prev[i + 1][0]):
                    prev[i] = prev[i-1] + prev[i] + prev[i+1]
                    sym = prev[i + 1]
                    del prev[i + 1]
                    del prev[i - 1]
                    self.dfs(prev, i - 1)
                    prev.insert(i - 1, sym)
                    prev.insert(i + 1, sym)
                    prev[i] = prev[i][1:len(prev[i]) - 1]
            if (self.isPalindrom(prev[i] + prev[i + 1])):
                sym = prev[i + 1]
                prev[i] = prev[i] + prev[i + 1]
                del prev[i + 1]
                self.dfs(prev, i)
                prev[i] = prev[i][:len(prev[i]) - 1]
                prev.insert(i + 1, sym)

    def partition(self, s: str):
        self.answer = []
        ans = []
        for c in s:
            ans.append(c)
        self.dfs(ans.copy(), 0)
        self.distinct()
        return self.answer
sol = Solution()
ans = sol.partition("fff")
print(ans)