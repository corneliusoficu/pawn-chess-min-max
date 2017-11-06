import ChessBoardFileReader

""" Let the white pawn be represented by 1 and the black pawn by 2.
We agree on the fact that the top of the chess board is the start point for the white pawns
and the bottom of the chess board is the start for the black ones. """


class ChessBoard:

    def __init__(self, filename="", from_file=False):
        if from_file:
            self.chess_board = ChessBoardFileReader.extract_chess_board_from_file(filename)
        else:
            self.chess_board = ChessBoard.get_standard_chess_board()

    @staticmethod
    def get_standard_chess_board():
        black_pawns_line, empty_line, white_pawns_line = ChessBoard.construct_standard_lines()
        standard_chess_board = ChessBoard.build_standard_chess_board(black_pawns_line, empty_line, white_pawns_line)
        return standard_chess_board

    @staticmethod
    def build_standard_chess_board(black_pawns_line, empty_line, white_pawns_line):
        chess_board = [[] for i in range(0, 8)]
        chess_board[0] = empty_line
        chess_board[1] = white_pawns_line
        for index in range(2, 6):
            chess_board[index] = empty_line
        chess_board[6] = black_pawns_line
        chess_board[7] = empty_line
        return chess_board

    @staticmethod
    def construct_standard_lines():
        empty_line = []
        white_pawns_line = []
        black_pawns_line = []
        for index in range(0, 8):
            empty_line.append(0)
            white_pawns_line.append(1)
            black_pawns_line.append(2)
        return black_pawns_line, empty_line, white_pawns_line


if __name__ == '__main__':
    example_board = ChessBoard()
    print example_board.chess_board
