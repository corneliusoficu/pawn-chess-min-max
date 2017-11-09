from chessboard import ChessBoard


class MoveValidator:

    def __init__(self, game):
        self.game = game
        self.error_message = ''

    @staticmethod
    def convert_character_to_integer(character):
        return ord(character) - ord('A')

    @staticmethod
    def is_move_valid(matrix, move_from, move_to, current_player_color):

        from_row = move_from[0]
        from_col = move_from[1]
        to_row = move_to[0]
        to_col = move_to[1]

        if MoveValidator.is_move_source_or_destination_outside_the_board(
            from_col, from_row, to_col, to_row, current_player_color
        ): return False

        # The source of the move "contains" no pawn to be moved === the value of that place is neither 1, nor 2
        if matrix[from_row][from_col] == 0:
            MoveValidator.process_error_message("No chess piece to move!", current_player_color)
            return False

        # Source is the same as destination
        if from_row == to_row and from_col == to_col:
            MoveValidator.process_error_message("You cannot move pawn to the same position from which you want to move!",current_player_color)
            return False

        # The pawn tries to move sideways
        if from_row == to_row:
            MoveValidator.process_error_message("The pawn cannot be moved sideways.",current_player_color)
            return False

        color_of_piece = matrix[from_row][from_col]

        # The current player tries to move opponent's piece
        if color_of_piece != current_player_color:
            MoveValidator.process_error_message("You cannot move the other player's pawn!",current_player_color)
            return False

        if color_of_piece == ChessBoard.WHITE_PAWN:  # the piece is white

            if from_row > to_row:  # wants to move backwards with one step
                MoveValidator.process_error_message("You cannot move the pawn backwards!",current_player_color)
                return False

            if from_col == to_col and from_row == to_row - 1:  # wants to move forward with one step
                if not MoveValidator.destination_is_empty(to_row, to_col):
                    MoveValidator.process_error_message("The destination {row}{column} you chose for the pawn is already taken!"
                                                        .format(row=move_to[0], column=move_to[1]))
                    return False

            elif from_col == to_col and from_row == 1 and to_row == 3:  # wants to move forward with two steps
                if not MoveValidator.destination_is_empty(to_row, to_col):
                    MoveValidator.process_error_message("The destination {row}{column} you chose for the pawn is already taken!"
                                                        .format(row=move_to[0], column=move_to[1]))
                    return False
                elif matrix[2][to_col] != 0:  # there is a piece between source and destination
                    MoveValidator.process_error_message("Cannot move pawn over the pawn in front!", current_player_color)
                    return False

                    # TODO: Register move as possible en passant capture for adversary

            elif abs(to_row - from_row) > 1 or abs(to_col - from_col) > 1: # wants to move too far away from current position
                MoveValidator.process_error_message("The destination {row}{column} is two far away for a valid move!"
                                                    .format(row = move_to[0], column = move_to[1]), current_player_color)
                return False

            elif (from_col == to_col - 1 or from_col == to_col + 1) and from_row == to_row - 1:
                # move forward, on the diagonal
                if MoveValidator.destination_is_empty(matrix,to_row, to_col):
                    MoveValidator.process_error_message(
                        "The destination {row}{column} you chose for the pawn is empty! (moving on diagonal)"
                            .format(row=move_to[0], column=move_to[1]), current_player_color)
                    return False
                elif matrix[to_row][to_col] == ChessBoard.WHITE_PAWN:
                    MoveValidator.process_error_message("White cannot capture white pawn!", current_player_color)
                    return False

                    # TODO: Check if en passant against adversary is possible

                    # TODO: Capture enemy pawn

        if color_of_piece == ChessBoard.BLACK_PAWN:  # the piece is black

            if from_row < to_row:  # wants to move backwards with one step
                MoveValidator.process_error_message("You cannot move the pawn backwards!", current_player_color)
                return False

            if from_col == to_col and from_row == to_row + 1:  # wants to move towards the white's start line with one step
                if not MoveValidator.destination_is_empty(matrix, to_row, to_col):
                    MoveValidator.process_error_message("The destination {row}{column} you chose for the pawn is already taken!"
                                                        .format(row=move_from[0], column=move_from[1]), current_player_color)
                    return False

            elif from_col == to_col and from_row == 6 and to_row == 4:  # wants to move forward with two steps
                if not MoveValidator.destination_is_empty(matrix, to_row, to_col):
                    MoveValidator.process_error_message("The destination {row}{column} you chose for the pawn is already taken!"
                                                        .format(row=move_from[0], column=move_from[1]), current_player_color)
                    return False
                elif matrix[5][to_col] != 0:  # there is a piece between source and destination
                    MoveValidator.process_error_message("Cannot move pawn over the pawn in front!", current_player_color)
                    return False

                    # TODO: Register move as possible en passant capture for adversary

            elif abs(to_row - from_row) > 1 or abs(to_col - from_col) > 1: # wants to move too far away from current position
                MoveValidator.process_error_message("The destination {row}{column} is too far away for a valid move!"
                                                    .format(row = move_to[0], column = move_to[1]), current_player_color)
                return False

            elif (from_col == to_col - 1 or from_col == to_col + 1) and from_row == to_row + 1:
                # move forward, on the diagonal
                if MoveValidator.destination_is_empty(matrix, to_row, to_col):
                    MoveValidator.process_error_message(
                        "The destination {row}{column} you chose for the pawn is empty! (moving on diagonal)"
                            .format(row=move_to[0], column=move_to[1]), current_player_color)
                    return False
                elif matrix[to_row][to_col] == ChessBoard.BLACK_PAWN:
                    MoveValidator.process_error_message("Black cannot capture black pawn!",current_player_color)
                    return False

                    # TODO: Check if en passant against adversary is possible

                    # TODO: Capture enemy pawn
        return True

    @staticmethod
    def is_move_source_or_destination_outside_the_board(from_col, from_row, to_col, to_row, current_player_color):
        # Trying to move pawn outside the board
        if from_row < 0 or from_row >= ChessBoard.CHESS_BOARD_SIZE:
            MoveValidator.process_error_message("Source row, {value}, is outside of the board!"
                                                .format(value=from_row), current_player_color)
            return True
        if from_col < 0 or from_col >= ChessBoard.CHESS_BOARD_SIZE:
            MoveValidator.process_error_message("Source column, {value}, is outside of the board!"
                                                .format(value=from_col), current_player_color)
            return True
        if to_row < 0 or to_row >= ChessBoard.CHESS_BOARD_SIZE:
            MoveValidator.process_error_message("Destination row, {value}, is outside of the board!"
                                                .format(value=to_row), current_player_color)
            return True
        if to_col < 0 or to_col >= ChessBoard.CHESS_BOARD_SIZE:
            MoveValidator.process_error_message("Destination column, {value}, is outside of the board!"
                                                .format(value=to_row), current_player_color)
            return True
        return False

    @staticmethod
    def destination_is_empty(matrix, to_row, to_col):
        return matrix[to_row][to_col] == 0

    @staticmethod
    def someone_won(matrix):
        if MoveValidator.white_reached_finish(matrix) \
                or MoveValidator.black_reached_finish(matrix):
            return True
        return False

    @staticmethod
    def black_reached_finish(matrix):
        if 2 in matrix[0]:
            return True
        return False

    @staticmethod
    def white_reached_finish(matrix):
        if 1 in matrix[ChessBoard.CHESS_BOARD_SIZE - 1]:
            return True
        return False

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

    @staticmethod
    def process_error_message(message, current_player_color):
        if current_player_color == 1:
            print message

