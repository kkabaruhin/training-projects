class Solution:
    def createAdjacencyList(self, numCourses, prerequisites):
        answer = {}
        for i in range(numCourses):
            answer[i] = []
        for item in prerequisites:
            answer[item[1]].append(item[0])
        return answer

    def dfs(self, graph, visited, recStack, k):
        if recStack[k]:
            return True
        if visited[k]:
            return False
        visited[k] = True
        recStack[k] = True

        if k in graph:
            for nei in graph[k]:
                if self.dfs(graph, visited, recStack, nei) == True:
                    return True

        recStack[k] = False
        return False

    def canFinish(self, numCourses: int, prerequisites):
        graph = self.createAdjacencyList(numCourses, prerequisites)
        visited = {}
        recStack = {}
        for i in range(numCourses):
            visited[i] = False
            recStack[i] = False
        for key in graph:
            if self.dfs(graph, visited, recStack, key):
                return True
        return False

sol = Solution()
print(sol.canFinish(2, [[1, 0]]))