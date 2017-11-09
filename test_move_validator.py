from chessboard import ChessBoard
from game import Game
from move_validator import MoveValidator
from pawn_possible_moves_generator import PawnMoveActions

if __name__ == '__main__':

    chessboard = ChessBoard("input-matrix.txt", True)
    chessboard.print_chessboard()
    game = Game(chessboard)
    validator = MoveValidator(game)
    # validator.is_move_valid((1,0),(1,1)) # sideways
    # print validator.error_message
    #
    # validator.is_move_valid((1,0),(0,0)) # white piece moves backwards
    # print validator.error_message
    #
    # validator.is_move_valid((2,1),(1,1)) # other's player pawn move
    # print validator.error_message
    #
    # validator.is_move_valid((1,1),(3,0)) # move over other pawn
    # print validator.error_message
    #
    # validator.is_move_valid((1,0),(4,3)) # illegal pawn move, too far
    # print validator.error_message
    #
    # print validator.can_white_capture_if_black_moves_two()
    #
    # print "did someone win?: ",validator.someone_won(chessboard.chess_board)
    generator = PawnMoveActions()
    print generator.generate_moves(2,(4,2))
    print generator.generate_validated_moves(2, (4, 2), chessboard.chess_board)

