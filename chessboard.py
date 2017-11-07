
""" Let the white pawn be represented by 1 and the black pawn by 2.
We agree on the fact that the top of the chess board is the start point for the white pawns
and the bottom of the chess board is the start for the black ones. """
from __future__ import print_function

import sys
from chess_board_file_reader import ChessBoardFileReader
from termcolor import colored, cprint


CHESS_BOARD_SIZE = 8

BLACK_PAWN_UNICODE = u'\u265F'
WHITE_PAWN_UNICODE = u'\u2659'
GREY_CHESSBOARD_CELL  = '\x1b[0;30;47m' + '%s' + '\x1b[0m'
WHITE_CHESSBOARD_CELL = '%s'
CUSTOM_WIDTH_SPACE = u'\u2003'
CELL_COLORS = [WHITE_CHESSBOARD_CELL, GREY_CHESSBOARD_CELL]

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

    def print_chessboard(self):
        color_index = 0
        color_inx = 0
        colors_size = len(CELL_COLORS)
        for chessboard_line in self.chess_board:
            color_index = color_inx
            for item in chessboard_line:
                chessboard_item = None
                if item == 1:
                    chessboard_item = WHITE_PAWN_UNICODE
                elif item == 2:
                    chessboard_item = BLACK_PAWN_UNICODE
                else:
                    chessboard_item = CUSTOM_WIDTH_SPACE
                chessboard_item = CELL_COLORS[color_index % colors_size] % format(chessboard_item)
                print (chessboard_item, end='')
                color_index += 1
            color_inx += 1
            print()


if __name__ == '__main__':
    example_board = ChessBoard()
    example_board.print_chessboard()

