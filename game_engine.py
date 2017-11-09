
class GameEngine:

    def __init__(self,game):
        self.game = game
        self.chessboard = self.game.chessboard
        self.move_validator = game.move_validator


    def is_draw(self):

        for row in range(0, self.chessboard.CHESS_BOARD_SIZE):
            for col in range(0, self.chessboard.CHESS_BOARD_SIZE):

                current_piece = self.chessboard.chess_board[row][col]

                current_row = row
                curret_col = chr(ord('A') + col)

                if current_piece == self.chessboard.WHITE_PAWN:
                    move_forward = [(current_row, curret_col),(current_row + 1, curret_col)]

                    if self.move_validator.is_move_valid(move_forward[0], move_forward[1]):
                        return False




        return True






    def find_next_best_move(self):
        pass
