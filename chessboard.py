import sys

from chessboard_file_reader import ChessBoardFileReader

BLACK_PAWN_UNICODE = u'\u265F'
WHITE_PAWN_UNICODE = u'\u2659'
GREY_CHESSBOARD_CELL = '\x1b[0;30;47m' + '%s' + '\x1b[0m'
WHITE_CHESSBOARD_CELL = '%s'
CUSTOM_WIDTH_SPACE = u'\u2003'
COL_INDEX_WHITE_SPACE = u'\u2004' + u'\u2006'
CELL_COLORS = [WHITE_CHESSBOARD_CELL, GREY_CHESSBOARD_CELL]

""" Let the white pawn be represented by 1 and the black pawn by 2.
We agree on the fact that the top of the chess board is the start point for the white pawns
and the bottom of the chess board is the start for the black ones. """
class ChessBoard:
    CHESS_BOARD_SIZE = 8
    WHITE_PAWN = 1
    BLACK_PAWN = 2

    def __init__(self, filename="", from_file=False):
        if from_file:
            self.chess_board = ChessBoardFileReader.extract_chess_board_from_file(filename)
        else:
            self.chess_board = ChessBoard.get_standard_chess_board()

    @staticmethod
    def get_standard_chess_board():
        standard_chess_board = ChessBoard.build_standard_chess_board()
        return standard_chess_board

    @staticmethod
    def build_standard_chess_board():
        chess_board = [[] for i in range(0, ChessBoard.CHESS_BOARD_SIZE)]
        chess_board[0] = ChessBoard.construct_line(0)
        chess_board[1] = ChessBoard.construct_line(ChessBoard.WHITE_PAWN)

        for index in range(2, ChessBoard.CHESS_BOARD_SIZE - 2):
            chess_board[index] = ChessBoard.construct_line(0)

        chess_board[ChessBoard.CHESS_BOARD_SIZE - 2] = ChessBoard.construct_line(ChessBoard.BLACK_PAWN)
        chess_board[ChessBoard.CHESS_BOARD_SIZE - 1] = ChessBoard.construct_line(0)
        return chess_board

    @staticmethod
    def construct_line(value):
        line = []

        for index in range(0, ChessBoard.CHESS_BOARD_SIZE):
            line.append(value)

        return line

    """Core piece move in the chess board matrix, 
    pawn chess game validation must be done beforehand!"""

    @staticmethod
    def move_piece(matrix, from_tuple, to_tuple):

            has_eaten_enemy_pawn = 0

            from_row = from_tuple[0]
            from_col = from_tuple[1]

            to_row = to_tuple[0]
            to_col = to_tuple[1]

            if matrix[to_row][to_col] != 0:
                has_eaten_enemy_pawn = 1

            matrix[to_row][to_col] = matrix[from_row][from_col]
            matrix[from_row][from_col] = 0

            return has_eaten_enemy_pawn

    def print_chessboard(self):

        color_index = 0
        color_count = 0
        colors_size = len(CELL_COLORS)
        row_index = 0
        col_index = ord('A')

        # Prints the column indexes in letters A,B,C...
        if len(self.chess_board) > 0:
            row_size = len(self.chess_board[0])
            if row_size > 0:
                # print(CUSTOM_WIDTH_SPACE, end='')
                sys.stdout.write(CUSTOM_WIDTH_SPACE)
                for index in range(0, row_size):
                    # print (chr(col_index) + COL_INDEX_WHITE_SPACE, end='')
                    sys.stdout.write(chr(col_index) + COL_INDEX_WHITE_SPACE)
                    col_index += 1

            print

        for chessboard_line in self.chess_board:
            color_index = color_count
            # print(row_index, end='')
            sys.stdout.write(str(row_index) + ' ')
            # print(' ', end='')
            row_index += 1
            for item in chessboard_line:

                chessboard_item = None
                if item == ChessBoard.WHITE_PAWN:
                    chessboard_item = WHITE_PAWN_UNICODE
                elif item == ChessBoard.BLACK_PAWN:
                    chessboard_item = BLACK_PAWN_UNICODE
                else:
                    chessboard_item = CUSTOM_WIDTH_SPACE

                chessboard_item = CELL_COLORS[color_index % colors_size] % format(chessboard_item)
                # print (chessboard_item, end='')
                sys.stdout.write(chessboard_item)
                color_index += 1
            color_count += 1
            print
        print


if __name__ == '__main__':
    example_board = ChessBoard()
    example_board.print_chessboard()

