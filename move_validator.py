from chessboard import ChessBoard


class MoveValidator:
    def __init__(self, game):
        self.game = game

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

            color_of_piece = self.game.chessboard[from_row][from_col]

            if color_of_piece == self.game.chessboard.WHITE_PAWN:  # the piece is white

                if from_row > to_row:  # wants to move backwards with one step
                    raise ("You cannot move the pawn backwards!")

                if from_col == to_col and from_row == to_row - 1:  # wants to move forward with one step
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_to[0], column=move_to[1]))

                elif from_col == to_col and from_row == 1 and to_row == 3:  # wants to move forward with two steps
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_to[0], column=move_to[1]))
                    elif self.game.chessboard[2][to_col] != 0:  # there is a piece between source and destination
                        raise Exception("Cannot move pawn over the pawn in front!")

                    # TODO: Register move as possible en passant capture for adversary

                elif (from_col == to_col - 1 or from_col == to_col + 1) and from_row == to_row + 1:
                    # move forward, on the diagonal
                    if self.destination_is_empty(to_row, to_col):
                        raise Exception(
                            "The destination {row}{column} you chose for the pawn is empty! (moving on diagonal)"
                                .format(row=move_to[0], column=move_to[1]))
                    elif self.game.chessboard.chess_board[to_row][to_col] == self.game.chessboard.BLACK_PAWN:
                        raise Exception("White cannot capture white pawn!")

                    # TODO: Check if en passant against adversary is possible

                    # TODO: Capture enemy pawn


            if color_of_piece == self.game.chessboard.BLACK_PAWN:  # the piece is white

                if from_row < to_row:  # wants to move backwards with one step
                    raise ("You cannot move the pawn backwards!")

                if from_col == to_col and from_row == to_row + 1:  # wants to move towards the white's start line with one step
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_from[0], column=move_from[1]))

                elif from_col == to_col and from_row == 6 and to_row == 4:  # wants to move forward with two steps
                    if not self.destination_is_empty(to_row, to_col):
                        raise Exception("The destination {row}{column} you chose for the pawn is already taken!"
                                        .format(row=move_from[0], column=move_from[1]))
                    elif self.game.chessboard[5][to_col] != 0:  # there is a piece between source and destination
                        raise Exception("Cannot move pawn over the pawn in front!")

                    # TODO: Register move as possible en passant capture for adversary

                elif from_col == to_col - 1 or from_col == to_col + 1 and from_row == to_row - 1:
                    # move forward, on the diagonal
                    if self.destination_is_empty(to_row, to_col):
                        raise Exception(
                            "The destination {row}{column} you chose for the pawn is empty! (moving on diagonal)"
                                .format(row=move_to[0], column=move_to[1]))
                    elif self.game.chessboard.chess_board[to_row][to_col] == self.game.chessboard.BLACK_PAWN:
                        raise Exception("Black cannot capture black pawn!")

                    # TODO: Check if en passant against adversary is possible

                    # TODO: Capture enemy pawn

            # self.game.chessboard.move_piece(move_from,move_to)

            return True

        except Exception as e:
            print e
            return False

    def is_player_moving_own_pawn(self, from_row, from_col):
        chessboard = self.game.chessboard.chess_board
        return chessboard[from_row][from_col] == self.game.player_piece[self.game.turn]

    def destination_is_empty(self, to_row, to_col):
        return self.game.chessboard[to_row][to_col] == 0
