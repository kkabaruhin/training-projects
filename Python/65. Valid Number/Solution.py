class Solution:
    def intNum(self, s: str) -> int:
        if (len(s) == 0 or (len(s) == 1 and (s[0] == '-' or s[0] == '+'))): return 0
        i = 0
        if (s[i] == '-' or s[i] == '+'): i += 1
        while (i < len(s) and s[i] >= '0' and s[i] <= '9'): i += 1
        if (len(s) > 1 and (s[0] == '-' or s[0] == '+') and i <= 1): return 0
        return i

    def decNum(self, s: str) -> int:
        if (len(s) == 0 or (len(s) == 1 and (s[0] == '-' or s[0] == '+' or s[0] == '.'))): return 0
        i = 0
        if (s[i] == '-' or s[i] == '+'): i += 1
        while (i < len(s) and s[i] >= '0' and s[i] <= '9'): i += 1
        wasADot = False
        if (i < len(s) and s[i] == '.'):
            i += 1
            wasADot = True
        while (i < len(s) and s[i] >= '0' and s[i] <= '9'): i += 1
        if (wasADot):
            return i
        else:
            return 0

    def isNumber(self, s: str) -> bool:
        n = len(s)
        a = self.intNum(s)
        b = self.decNum(s)
        if (a == n or b == n): return True
        if ((s[a] == 'E' or s[a] == 'e') and self.intNum(s[a + 1:]) + a + 1 == n): return True
        if ((s[b] == 'E' or s[b] == 'e') and self.intNum(s[b + 1:]) + b + 1 == n): return True
        return False
sol = Solution()
answer = sol.isNumber("2e0")
print(answer)