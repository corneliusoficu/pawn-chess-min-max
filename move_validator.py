from chessboard import ChessBoard


class MoveValidator:
    def __init__(self, game):
        self.game = game
        self.error_message = ''

    def is_move_valid(self, move_from, move_to):

        try:

            from_row = move_from[0]
            from_col = ord(move_from[1]) - ord('A')

            to_row = move_to[0]
            to_col = ord(move_to[1]) - ord('A')

            # Trying to move pawn outside the board
            if from_row < 0 or from_row >= ChessBoard.CHESS_BOARD_SIZE:
                raise Exception("Source row, {value}, is outside of the board!".format(value=from_row))
            if from_col < 0 or from_col >= ChessBoard.CHESS_BOARD_SIZE:
                raise Exception("Source column, {value}, is outside of the board!".format(value=from_col))
            if to_row < 0 or to_row >= ChessBoard.CHESS_BOARD_SIZE:
                raise Exception("Destination row, {value}, is outside of the board!".format(value=to_row))
            if to_col < 0 or to_col >= ChessBoard.CHESS_BOARD_SIZE:
                raise Exception("Destination column, {value}, is outside of the board!".format(value=to_row))

            # The source of the move "contains" no pawn to be moved === the value of that place is neither 1, nor 2
            if self.game.chessboard.chess_board[from_row][from_col] == 0:
                raise Exception("No chess piece to move!")

            # The current player tries to move opponent's piece
            if not self.is_player_moving_own_pawn(from_row, from_col):
                raise Exception("You cannot move the other player's pawn!")

            # Source is the same as destination
            if from_row == to_row and from_col == to_col:
                raise Exception("You cannot move pawn to the same position from which you want to move!")

            # The pawn tries to move sideways
            if from_row == to_row:
                raise Exception("The pawn cannot be moved sideways.")

            color_of_piece = self.game.chessboard.chess_board[from_row][from_col]

            if color_of_piece == ChessBoard.WHITE_PAWN:  # the piece is white

                if from_row > to_row:  # wants to move backwards with one step
                    raise Exception("You cannot move the pawn backwards!")

                if from_col == to_col and from_row == to_row - 1:  # wants to move forward with one step
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_to[0], column=move_to[1]))

                elif from_col == to_col and from_row == 1 and to_row == 3:  # wants to move forward with two steps
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_to[0], column=move_to[1]))
                    elif self.game.chessboard.chess_board[2][to_col] != 0:  # there is a piece between source and destination
                        raise Exception("Cannot move pawn over the pawn in front!")

                        # TODO: Register move as possible en passant capture for adversary

                elif abs(to_row - from_row) > 1 or abs(to_col - from_col) > 1: # wants to move too far away from current position
                    raise Exception("The destination {row}{column} is two far away for a valid move!".format(row = move_to[0], column = move_to[1]))

                elif (from_col == to_col - 1 or from_col == to_col + 1) and from_row == to_row + 1:
                    # move forward, on the diagonal
                    if self.destination_is_empty(to_row, to_col):
                        raise Exception(
                            "The destination {row}{column} you chose for the pawn is empty! (moving on diagonal)"
                                .format(row=move_to[0], column=move_to[1]))
                    elif self.game.chessboard.chess_board[to_row][to_col] == ChessBoard.WHITE_PAWN:
                        raise Exception("White cannot capture white pawn!")

                        # TODO: Check if en passant against adversary is possible

                        # TODO: Capture enemy pawn


            if color_of_piece == ChessBoard.BLACK_PAWN:  # the piece is white

                if from_row < to_row:  # wants to move backwards with one step
                    raise Exception("You cannot move the pawn backwards!")

                if from_col == to_col and from_row == to_row + 1:  # wants to move towards the white's start line with one step
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_from[0], column=move_from[1]))

                elif from_col == to_col and from_row == 6 and to_row == 4:  # wants to move forward with two steps
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_from[0], column=move_from[1]))
                    elif self.game.chessboard.chess_board[5][to_col] != 0:  # there is a piece between source and destination
                        raise Exception("Cannot move pawn over the pawn in front!")

                        # TODO: Register move as possible en passant capture for adversary

                elif abs(to_row - from_row) > 1 or abs(to_col - from_col) > 1: # wants to move too far away from current position
                    raise Exception("The destination {row}{column} is two far away for a valid move!".format(row = move_to[0], column = move_to[1]))

                elif from_col == to_col - 1 or from_col == to_col + 1 and from_row == to_row - 1:
                    # move forward, on the diagonal
                    if self.destination_is_empty(to_row, to_col):
                        raise Exception(
                            "The destination {row}{column} you chose for the pawn is empty! (moving on diagonal)"
                                .format(row=move_to[0], column=move_to[1]))
                    elif self.game.chessboard.chess_board[to_row][to_col] == ChessBoard.BLACK_PAWN:
                        raise Exception("Black cannot capture black pawn!")

                        # TODO: Check if en passant against adversary is possible

                        # TODO: Capture enemy pawn

            # self.game.chessboard.move_piece(move_from,move_to)

            self.error_message = ''
            return True

        except Exception as e:
            self.error_message = e
            return False

    def is_player_moving_own_pawn(self, from_row, from_col):
        chessboard = self.game.chessboard.chess_board
        return chessboard[from_row][from_col] == self.game.player_piece[self.game.turn]

    def destination_is_empty(self, to_row, to_col):
        return self.game.chessboard.chess_board[to_row][to_col] == 0

    def can_white_capture_if_black_moves_two(self):
        if self.game.was_last_move_a_two_step_move and self.game.turn == 0: # human == 0 == white
            black_piece_col = ord(self.game.position_of_two_steps_pawn[1]) - ord('A')
            # if there is a white piece to the left or to the right of that black piece that moved two
            if black_piece_col-1 > 0 \
                    and self.game.chessboard.chess_board[4][black_piece_col-1] == ChessBoard.WHITE_PAWN:
                return True
            if black_piece_col + 1 < ChessBoard.CHESS_BOARD_SIZE \
                    and self.game.chessboard.chess_board[4][black_piece_col+1] == ChessBoard.WHITE_PAWN:
                return True
        return False

    def can_black_capture_if_white_moves_two(self):
        if self.game.was_last_move_a_two_step_move and self.game.turn == 1: # ai == 1 == black
            white_piece_col = ord(self.game.position_of_two_steps_pawn[1]) - ord('A')
            # if there is a black piece to the left or to the right of that white piece that moved 2 steps
            if white_piece_col-1 > 0 \
                    and self.game.chessboard.chess_board[4][white_piece_col-1] == ChessBoard.BLACK_PAWN:
                return True
            if white_piece_col + 1 < ChessBoard.CHESS_BOARD_SIZE \
                    and self.game.chessboard.chess_board[4][white_piece_col+1] == ChessBoard.BLACK_PAWN:
                return True
        return False

    def black_reached_finish(self):
        if 2 in self.game.chessboard.chess_board[ChessBoard.CHESS_BOARD_SIZE-1]:
            return True
        return False

    def white_reached_finish(self):
        if 1 in self.game.chessboard.chess_board[ChessBoard.CHESS_BOARD_SIZE-1]:
            return True
        return False
