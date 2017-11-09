import random

from chessboard import ChessBoard
from pawn_possible_moves_generator import PawnMoveActions


class GameEngine:

    FILTER_PERCERNT = 0.25

    def __init__(self,game):
        self.game = game
        self.chessboard = self.game.chessboard
        self.move_validator = game.move_validator


    def generate_all_legal_moves(self, chessboard, pawn_type):

        probable_valid_moves = []
        for row in range(0, ChessBoard.CHESS_BOARD_SIZE):
            for col in range(0, ChessBoard.CHESS_BOARD_SIZE):
                if pawn_type == chessboard[row][col]:

                    list_moves = PawnMoveActions.generate_moves(pawn_type, [row, col])
                    for move in list_moves:
                        move_from = (row, col)
                        move_to = (move[0], move[1])
                        if self.move_validator.is_move_valid(chessboard, move_from, move_to, pawn_type):
                            possible_move = [move_from, move_to]
                            probable_valid_moves.append(possible_move)

        return probable_valid_moves


    def generate_random_moves(self, chessboard, pawn_type):

        probable_valid_moves = self.generate_all_legal_moves(chessboard, pawn_type)

        len_prob_moves = len(probable_valid_moves)
        number_of_moves = int(GameEngine.FILTER_PERCERNT * len_prob_moves)
        chosen_indexes = []
        chosen_move = 0
        while(chosen_move <= number_of_moves):
            random_index = random.randint(0, len_prob_moves - 1)
            if random_index not in chosen_indexes:
                chosen_indexes.append(random_index)
                chosen_move += 1


        chosen_valid_moves = [probable_valid_moves[indx] for indx in chosen_indexes]
        return chosen_valid_moves


    def is_draw(self, matrix):
        all_legal_moves_white = self.generate_all_legal_moves(matrix,ChessBoard.WHITE_PAWN)
        all_legal_moves_black = self.generate_all_legal_moves(matrix,ChessBoard.BLACK_PAWN)

        return len(all_legal_moves_white) == 0 and len(all_legal_moves_black) == 0


    def is_win(self, matrix):
        if self.white_reached_finish(matrix) \
                or self.black_reached_finish(matrix):
            return True
        return False


    def black_reached_finish(self, matrix):
        if 2 in matrix[0]:
            return True
        return False


    def white_reached_finish(self, matrix):
        if 1 in matrix[ChessBoard.CHESS_BOARD_SIZE - 1]:
            return True
        return False




