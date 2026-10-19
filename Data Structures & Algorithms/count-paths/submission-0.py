class Solution:
    def getPath(self,m, n, i, j, paths):

        # Walls
        if i == m or j == n:
            return 0

        # End case
        if i == m-1 and j == n-1:
            return 1

        # Get cached
        if paths[i][j] > 0:
            return paths[i][j]

        # Calculate path
        paths[i][j] = self.getPath(m, n, i+1, j, paths) + self.getPath(m, n, i, j+1, paths)

        return paths[i][j]

    def uniquePaths(self, m: int, n: int) -> int:

        # Top down DP
        paths = [[0] * n for i in range(m)]
        # print(paths)
        path = self.getPath(m, n, 0, 0, paths)
        # print(path)

        return path



        