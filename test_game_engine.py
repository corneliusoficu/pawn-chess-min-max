from chessboard import ChessBoard
from game import Game
from game_engine import GameEngine


if __name__ == '__main__':
    chessboard = ChessBoard("input-matrix.txt", True)
    chessboard.print_chessboard()
    game = Game(chessboard)
    game_engine = GameEngine(game)

    print game_engine.is_draw(chessboard.chess_board)