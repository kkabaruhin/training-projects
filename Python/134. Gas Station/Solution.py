class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        i = 0
        start = i
        circle = 0
        currTank = 0
        while True:
            currTank = currTank + gas[i] - cost[i]
            if (currTank < 0 and circle > 0): return -1
            if (currTank < 0):
                start = (i + 1) % n
            if (i == n - 1):
                circle += 1
            if (circle > 1):
                return start
            i = (i + 1) % n
sol = Solution
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(sol, gas, cost))