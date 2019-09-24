'''
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # 标志位初始化为False
        flag = [False] * len(matrix)
        path = list(path)
        for i in range(rows):
            for j in range(cols):
                # 循环遍历二维数组，找到起点等于str第一个元素的值，在递归判断四周是否有符合条件的——回溯法
                if self.judge(matrix, i, j, rows, cols, flag, path, 0):
                    return True
        return False

    # judge（初始矩阵，索引行坐标i， 索引列坐标j， 矩阵函数， 矩阵列数， 标志位， 待判断字符串， 遍历字符串
    def judge(self, matrix, i, j, rows, cols, flag, s, k):
        # 先根据i , j 计算匹配的第一个元素转为一维数组的位置
        index = i * cols + j
        # 递归终止条件
        if i<0 or j<0 or i>=rows or j>= cols or matrix[index] != s[k] or flag[index] == True:
            return False
        # 若k已经到达s末尾了，说明之前的都已经匹配成功了， 直接返回True
        if k == len(s)-1:
            return True
        # 回溯递归寻找，每次找到了，k += 1， 找不到就还原
        if self.judge(matrix, i - 1, j, rows, cols, flag, s, k + 1) or \
                self.judge(matrix, i + 1, j, rows, cols, flag, s, k + 1) or \
                self.judge(matrix, i, j - 1, rows, cols, flag, s, k + 1) or \
                self.judge(matrix, i, j + 1, rows, cols, flag, s, k + 1):

            return True
        # 走到这，说明这一条路不通，还原，再试其他的路径
        flag[index] = False
        return False
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(list(matrix),rows,cols,path[1:],i,j):
                        return True
        return False
    def find(self,matrix,rows,cols,path,i,j):
        if not path:
            return True
        matrix[i*cols+j]='0'
        if j+1<cols and matrix[i*cols+j+1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j+1)
        elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j-1)
        elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i+1,j)
        elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i-1,j)
        else:
            return False

if __name__=='__main__':
    s = Solution()
    matrix = 'abcesfcsadee'
    cols = 4
    rows = 3
    string = "bcced"
    print(s.hasPath(matrix,cols, rows,string))