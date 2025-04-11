
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        answer = 0
        n = 1
        cnt = (right - left + 1)
        while n <= right:
            if cnt > n:
                digit = 0
            else:
                leftBit = left // n % 2
                rightBit = right // n % 2
                digit = leftBit * rightBit
            answer = answer + digit * n
            n *= 2
        return answer
sol = Solution()
print(sol.rangeBitwiseAnd(6, 12))
                            #0110
                            #0111
                            #1000
                            #1001
                            #1010
                            #1011
                            #1100