from chessboard import ChessBoard
from move_validator import MoveValidator


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

    @staticmethod
    def generate_validated_moves(pawn_color, pawn_position_as_integers, matrix):
        unvalidated_possible_moves = PawnMoveActions.generate_moves(
            pawn_color=pawn_color, pawn_position_as_integers=pawn_position_as_integers
        )
        validated_moves = []
        for possible_move in unvalidated_possible_moves:
            if MoveValidator.is_move_valid(matrix, pawn_position_as_integers, possible_move, pawn_color):
                validated_moves.append(possible_move)
        return validated_moves
