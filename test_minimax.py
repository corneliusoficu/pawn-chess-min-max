from chessboard import ChessBoard
from game import Game
from minmax import MinMax

if __name__ == '__main__':
    chess_board = ChessBoard()
    game = Game(chess_board)
    game.turn = 1
    mini_max = MinMax(game, None)

    # mini_max.generate_legal_moves(chess_board.chess_board,ChessBoard.BLACK_PAWN)
    mini_max.find_best_move_using_minimax()