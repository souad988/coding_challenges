'''
36. Valid Sudoku  Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''



def isValidSudoku(self,board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        horizontal = []
        vertical = []
        cube = []
        for i in range(len(board)):
          horizontal.append({})
        for i in range(len(board[0])):
          vertical.append({})
        for i in range(int((len(board[0])*len(board))/9)):
          cube.append({})
        cube_i = 0
        cube_j = 0
        for i in range(len(board)):
            
            cube_i = i//3 * int(len(board[0])/3)
            for j in range(len(board[0])):
                cube_j = j//3
                if board[i][j] in horizontal[i]:
                    return False
                else: 
                    if board[i][j] != '.':
                      horizontal[i][board[i][j]] = True
                if board[i][j] in vertical[j]:
                    return False
                else:
                    if board[i][j] != '.':
                      vertical[j][board[i][j]] = True
                if board[i][j] in cube[cube_i + cube_j]:
                    return False
                else:
                    if board[i][j] != '.':
                      cube[cube_i + cube_j][board[i][j]] = True 
        return True 