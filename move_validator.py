from chessboard import ChessBoard


class MoveValidator:
    def __init__(self, chessboard, game):
        self.chessboard = chessboard
        self.game = game

    def player_moves_own_pawn(self, from_row, from_col):


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

            if self.chessboard[from_row][from_col] == 0:
                raise Exception("No chess piece to move!")



            return True

        except Exception as e:
            print e
            return False

