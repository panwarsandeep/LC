class Solution:
    def validTicTacToe(self, board):
        def is_won(board, p):
            for i in range(3):
                if all(board[i][j] == p for j in range(3)):
                    return True
                if all(board[j][i] == p for j in range(3)):
                    return True
            if all(board[i][i] == p for i in range(3)) or \
                all(board[i][2-i] == p for i in range(3)):
                return True
            return False
        
        flat_str = ''.join(board)
        no_x = flat_str.count('X')
        no_o = flat_str.count('O')
        print(no_x, no_o)
        if no_x < no_o or no_x - no_o > 1:
            return False
        for i in range(3):
            board[i] = list(board[i])
        if is_won(board, 'X') and no_x != no_o + 1:
            return False
        if is_won(board, 'O') and no_x != no_o:
            return False

        return True

   

if __name__ == '__main__':
    sol = Solution()
    
    b = ["O  ", "   ", "   "]
    b = ["XOX", "O O", "XOX"]
    b = ["XXX","OOX","OOX"]
    print(b)
    r = sol.validTicTacToe(b)
    print(r)
    

