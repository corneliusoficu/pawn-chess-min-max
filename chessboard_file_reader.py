
class ChessBoardFileReader:

    def __init__(self):
        pass

    @staticmethod
    def extract_chess_board_from_file(filename):
        descriptor = open(filename, "r")
        return [map(int,line.split(",")) for line in descriptor]

    @staticmethod
    def print_chess_board(chess_board):
        for line in chess_board:
            print line


if __name__ == '__main__':
    chess_board = ChessBoardFileReader.extract_chess_board_from_file("input-matrix.txt")
    ChessBoardFileReader.print_chess_board(chess_board)