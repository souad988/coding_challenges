# @param {Character[][]} board
# @return {Boolean}
def is_valid_sudoku(board)
    vertical = []
    horizontal = []
    cube = []
    
    (0...board.length).step(1) do |a|
      horizontal.append({})
    end
    
    (0...board[0].length).step(1) do |a|
      vertical.append({}) 
    end
    
    (0...(board[0].length * board.length) / 9).step(1) do |a|
      cube.append({})  
    end
    
    cube_i = 0
    cube_j = 0
    
    (0...board.length).step(1) do |i|
      cube_i = (i / 3) * (board[0].length / 3)
      
      (0...board[0].length).step(1) do |j|
        cube_j = j / 3
        
        if horizontal[i].include?(board[i][j])
          return false
        else
          horizontal[i][board[i][j]] = true if board[i][j] != '.'
        end
  
        if  vertical[j].include?(board[i][j])
          return false
        else
          vertical[j][board[i][j]] = true if board[i][j] != '.'
        end 
  
        if  cube[cube_i + cube_j].include?(board[i][j])
          return false
        else
          cube[cube_i + cube_j][board[i][j]] = true if board[i][j] != '.'
        end 
      end
    end      
    
    return true             
  end