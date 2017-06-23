class Board:
    board = [['X',' ','O'],[' ',' ',' '],['X', 'X', 'O']]

    def print_board(self):
        for row in self.board:
            row_string = ''
            for index, space in enumerate(row):
                if index == 0:
                    saved_string = row_string + space + '|'
                elif index == 1:
                    saved_string = saved_string + space + '|'
                else:
                    print saved_string + space

    def place_piece(self, character, row, row_position):
        self.board[row][row_position] = character

    def ai_move(self, character):
        for row in self.board:
            for index, space in enumerate(row):
                if space == ' ':
                    row[index] = character
                    return

board = Board()
board.ai_move('O')
board.place_piece('X', 1, 2)
board.print_board()
