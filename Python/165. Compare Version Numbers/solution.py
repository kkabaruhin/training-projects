class Solution:
    def compareOneVersion(self, version1, version2):
        if ('.' in version1):
            dotIndex1 = version1.index('.')
            num1 = int(version1[:dotIndex1])
        else:
            if (version1 == ''):
                num1 = 0
            else:
                num1 = int(version1)
        if ('.' in version2):
            dotIndex2 = version2.index('.')
            num2 = int(version2[:dotIndex2])
        else:
            if (version2 == ''):
                num2 = 0
            else:
                num2 = int(version2)
        if (num1 < num2): return -1
        if (num1 > num2): return 1
        return 0
    def compareVersion(self, version1: str, version2: str) -> int:
        while True:
            ans = self.compareOneVersion(version1, version2)
            if ans != 0:
                return ans
            if  '.' not in version1 and '.' not in version2:
                return 0
            if '.' in version1:
                version1 = version1[version1.index('.') + 1:]
            else:
                version1 = ''
            if '.' in version2:
                version2 = version2[version2.index('.') + 1:]
            else:
                version2 = ''
sol = Solution()
print(sol.compareVersion("1.0.1","1"))