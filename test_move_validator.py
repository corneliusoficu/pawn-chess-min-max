from chessboard import ChessBoard
from game import Game
from move_validator import MoveValidator

if __name__ == '__main__':
    chessboard = ChessBoard("input-matrix.txt", True)
    chessboard.print_chessboard()
    game = Game(chessboard)
    validator = MoveValidator(game)
    #validator.is_move_valid((1,'A'),(1,'B')) # sideways
    validator.is_move_valid((1,'A'),(0,'A')) # white piece moves backwards
