from chessboard import ChessBoard


class MoveValidator:
    def __init__(self, game):
        self.game = game

    def is_player_moving_own_pawn(self, from_row, from_col):
        chessboard = self.game.chessboard.chess_board

        if chessboard[from_row][from_col] != self.game.player_piece[self.game.turn]:
            return False

        return True

    def is_move_valid(self, move_from, move_to):

        try:

            from_row = move_from[0]
            from_col = ord(move_from[1]) - ord('A')

            to_row = move_to[0]
            to_col = ord(move_to[1]) - ord('A')

            if from_row < 0 or from_row >= ChessBoard.CHESS_BOARD_SIZE or \
                            from_col < 0 or from_col >= ChessBoard.CHESS_BOARD_SIZE or \
                            to_row < 0 or to_row >= ChessBoard.CHESS_BOARD_SIZE or \
                            to_col < 0 or to_col >= ChessBoard.CHESS_BOARD_SIZE:
                raise Exception("Move outside of the board!")

            if self.game.chessboard.chess_board[from_row][from_col] == 0:
                raise Exception("No chess piece to move!")

            if not self.is_player_moving_own_pawn(from_row,from_col):
                raise Exception("You cannot move the other player's pawn!")

            if is_move_2_steps_from_base()

            self.game.chessboard.move_piece(move_from,move_to)

            return True

        except Exception as e:
            print e
            return False

