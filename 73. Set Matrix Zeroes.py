class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowlen=len(matrix)
        collen=len(matrix[0])
        row=[]
        col=[]
        for i in range(rowlen):            
            for j in range(collen):
                if matrix[i][j]==0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in range(rowlen):
            if i in row:
                for j in range(collen):
                    matrix[i][j]=0
        for j in range(collen):
            if j in col:
                for i in range(rowlen):
                    matrix[i][j]=0
