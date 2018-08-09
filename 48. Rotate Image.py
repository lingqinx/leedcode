class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix)):
            #print matrix[i]
            matrix[i]=matrix[i][::-1]
        """    
        #zip(matrix)实现行列互换
        matrix[::] = zip(*matrix[::-1])
