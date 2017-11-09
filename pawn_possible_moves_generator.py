from chessboard import ChessBoard


class PawnMoveActions:

    @staticmethod
    def generate_moves(pawn_color, pawn_position_as_integers):
        current_row = pawn_position_as_integers[0]
        current_col = pawn_position_as_integers[1]
        unvalidated_possible_moves = []
        if pawn_color == ChessBoard.WHITE_PAWN:
            unvalidated_possible_moves.append((current_row + 1, current_col))  # straight, one step
            unvalidated_possible_moves.append((current_row + 2, current_col))  # straight, two steps
            unvalidated_possible_moves.append((current_row + 1, current_col + 1))  # diagonal, right
            unvalidated_possible_moves.append((current_row + 1, current_col - 1))  # diagonal, left
        elif pawn_color == ChessBoard.BLACK_PAWN:
            unvalidated_possible_moves.append((current_row - 1, current_col))  # straight, one step
            unvalidated_possible_moves.append((current_row - 2, current_col))  # straight, two steps
            unvalidated_possible_moves.append((current_row - 1, current_col - 1))  # diagonal, left
            unvalidated_possible_moves.append((current_row - 1, current_col + 1))  # diagonal, right
        return unvalidated_possible_moves
