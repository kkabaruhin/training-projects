class Solution:
    answer = []
    def makeAnswer(self, dp, i, s, currs):
        if i == 0:
            self.answer.append(currs[: len(currs) - 1])
            return
        for j in dp[i]:
            self.makeAnswer(dp, j, s, s[j:i] + ' ' + currs)
    def wordBreak(self, s, wordDict):
        hashTable = {}
        self.answer = []
        n = len(s)
        for word in wordDict:
            hashTable[word] = True
        dp = []
        for i in range(n + 1):
            dp.append([])
        for i in range(n):
            for j in range(i + 1):
                if ((dp[j] != [] and s[j: i + 1] in hashTable)):
                    dp[i + 1].append(j)
                elif (j == 0 and s[j: i + 1] in hashTable):
                    dp[i + 1].append(0)
        self.makeAnswer(dp, n, s, "")
        return self.answer
sol = Solution()
wordDict = ["a", "b"]
s = "ab"
print(sol.wordBreak(s, wordDict))