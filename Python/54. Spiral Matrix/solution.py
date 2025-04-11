class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        circle = 0
        i = 0
        j = 0
        answer = []
        while (len(answer) < n * m):
            i = circle
            for j in range(circle, m - circle):
                if (len(answer) < n * m):
                    answer.append(matrix[i][j])
            j = m - circle - 1
            for i in range(circle + 1, n - circle):
                if (len(answer) < n * m):
                    answer.append(matrix[i][j])
            i = n - circle - 1
            for j in range(m - circle - 2, circle - 1, -1):
                if (len(answer) < n * m):
                    answer.append(matrix[i][j])
            j = circle
            for i in range(n - circle - 2, circle, -1):
                if (len(answer) < n * m):
                    answer.append(matrix[i][j])
            circle += 1
        return answer

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
answer = sol.spiralOrder(matrix)
print(answer)
