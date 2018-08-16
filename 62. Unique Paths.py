class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        matrix=[[0]*n for i in range(m)]
        for i in range(1,n):
            matrix[0][i] = 1
        for i in range(1,m):
            matrix[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
        return matrix[m-1][n-1]
