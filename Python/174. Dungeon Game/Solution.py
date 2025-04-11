class Solution:
    #(minHP, CurrHP)
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dpTable = []
        for i in range(m):
            dpTable.append([])
            for j in range(n):
                dpTable[i].append([])
        dpTable[0][0] = [(dungeon[0][0], dungeon[0][0])]
        for i in range(1, m):
            prevMin = dpTable[i - 1][0][0][0]
            prevHP = dpTable[i - 1][0][0][1]
            currHP = prevHP + dungeon[i][0]
            dpTable[i][0] = [(min(prevMin, currHP), currHP)]
        for j in range(1, n):
            prevMin = dpTable[0][j - 1][0][0]
            prevHP = dpTable[0][j - 1][0][1]
            currHP = prevHP + dungeon[0][j]
            dpTable[0][j] = [(min(prevMin, currHP), currHP)]
        for i in range(1,m):
            for j in range(1,n):
                for elem1 in dpTable[i - 1][j]:
                    needToTake = True
                    for elem2 in dpTable[i][j - 1]:
                        if elem2[0] > elem1[0] and elem2[1] > elem1[1]:
                            needToTake = False
                            break
                    if (needToTake):
                        prevMin = elem1[0]
                        prevHP = elem1[1]
                        currHP = prevHP + dungeon[i][j]
                        dpTable[i][j].append((min(prevMin, currHP), currHP))
                for elem1 in dpTable[i][j - 1]:
                    needToTake = True
                    for elem2 in dpTable[i - 1][j]:
                        if elem2[0] > elem1[0] and elem2[1] > elem1[1]:
                            needToTake = False
                            break
                    if (needToTake):
                        prevMin = elem1[0]
                        prevHP = elem1[1]
                        currHP = prevHP + dungeon[i][j]
                        dpTable[i][j].append((min(prevMin, currHP), currHP))
        answer = -9999999999999
        for elem in dpTable[m - 1][n - 1]:
            answer = max(answer, elem[0])
        return abs(answer) + 1

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
sol = Solution()
print(sol.calculateMinimumHP(dungeon))