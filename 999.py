class Solution:
    def numRookCaptures(self, board: 'List[List[str]]') -> 'int':
        # 有一个白色车（rook）
        pawn = 0
        for i in range(len(board)):
            if 'R' in board[i]:
                #print(i,board[i].index('R'))
                Ri, Rj = i, board[i].index('R')
                break
        # 上
        for i in range(Ri, 0, -1):
            if board[i][Rj] == 'B':
                break
            if board[i][Rj] == 'p':
                pawn += 1
                break
        # 下
        for i in range(Ri, len(board)):
            if board[i][Rj] == 'B':
                break
            if board[i][Rj] == 'p':
                pawn += 1
                break
        # 左
        for j in range(Rj, 0, -1):
            if board[Ri][j] == 'B':
                break
            if board[Ri][j] == 'p':
                pawn += 1
                break
        # 右
        for j in range(Rj, len(board[Ri])):
            if board[Ri][j] == 'B':
                break
            if board[Ri][j] == 'p':
                pawn += 1
                break
        return pawn

if __name__ == '__main__':
    s = Solution()
    # A = [[".",".",".",".",".",".",".","."],
    #      [".",".",".","p",".",".",".","."],
    #      [".",".",".","R",".",".",".","p"],
    #      [".",".",".",".",".",".",".","."],
    #      [".",".",".",".",".",".",".","."],
    #      [".",".",".","p",".",".",".","."],
    #      [".",".",".",".",".",".",".","."],
    #      [".",".",".",".",".",".",".","."]]
    A = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
     [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    #A = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(s.numRookCaptures(A))