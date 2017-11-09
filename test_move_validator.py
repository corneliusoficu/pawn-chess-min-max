from chessboard import ChessBoard
from game import Game
from move_validator import MoveValidator

if __name__ == '__main__':
    chessboard = ChessBoard("input-matrix.txt", True)
    chessboard.print_chessboard()
    game = Game(chessboard)
    validator = MoveValidator(game)
    validator.is_move_valid((1,'A'),(1,'B')) # sideways
    print validator.error_message

    validator.is_move_valid((1,'A'),(0,'A')) # white piece moves backwards
    print validator.error_message

    validator.is_move_valid((2,'B'),(1,'B')) # other's player pawn move
    print validator.error_message

    validator.is_move_valid((1,'B'),(3,'B')) # move over other pawn
    print validator.error_message

    validator.is_move_valid((1,'A'),(4,'D')) # illegal pawn move, too far
    print validator.error_message

    print validator.can_white_capture_if_black_moves_two()




