import copy
import random

from chessboard import ChessBoard
from game import Player, Game
from pawn_possible_moves_generator import PawnMoveActions


class Position:
    def __init__(self, chessboard, to_move, current_move = None):
        self.to_move = to_move
        self.chessboard = copy.deepcopy(chessboard)
        self.current_move = current_move

class MinMax:

    TREE_HEIGHT = 4
    FILTER_PERCERNT = 0.50

    def __init__(self, game, move_validator):

        self.chessboard = game.chessboard.chess_board
        #self.move_validator = move_validator
        self.game = game
        self.move_validator = game.move_validator

    def find_best_move_using_minimax(self):
        position = Position(self.chessboard, ChessBoard.BLACK_PAWN)
        self.minimax(position, MinMax.TREE_HEIGHT)


    def minimax(self, position, depth):
        if depth == 0:
            return self.evaluate_position(position)
        else:
            if position.to_move == ChessBoard.BLACK_PAWN:
                best_score = -float("inf")
                best_move = None
                valid_moves = self.generate_legal_moves(position.chessboard,position.to_move)
                for move in valid_moves:
                    new_position = self.make_move_for_position(position,move)
                    score, move = self.minimax(new_position, depth - 1)
                    if score > best_score:
                        best_score = score
                        best_move = move
                return (best_score, best_move)


    def evaluate_position(self, position):
        pass

    def generate_legal_moves(self, chessboard, pawn_type):

        probable_valid_moves = []

        for row in range(0,ChessBoard.CHESS_BOARD_SIZE):
            for col in range(0, ChessBoard.CHESS_BOARD_SIZE):
                if pawn_type == chessboard[row][col]:
                    #TODO pick with certain probability
                    list_moves = PawnMoveActions.generate_moves(pawn_type, [row,col])
                    for move in list_moves:
                        move_from = (row,col)
                        move_to = (move[0], move[1])
                        if self.move_validator.is_move_valid(chessboard, move_from, move_to, pawn_type):
                            possible_move = [move_from, move_to]
                            probable_valid_moves.append(possible_move)


        len_prob_moves = len(probable_valid_moves)
        number_of_moves = int(MinMax.FILTER_PERCERNT * len_prob_moves)
        chosen_indexes = []
        chosen_move = 0
        while(chosen_move <= number_of_moves):
            random_index = random.randint(0, len_prob_moves - 1)
            if random_index not in chosen_indexes:
                chosen_indexes.append(random_index)
                chosen_move += 1


        chosen_valid_moves = [probable_valid_moves[indx] for indx in chosen_indexes]
        return chosen_valid_moves

    def make_move_for_position(self,position, move):

        new_chessboard_matrix = copy.deepcopy(position.chessboard)
        ChessBoard.move_piece(new_chessboard_matrix,move[0],move[1])
        if position.to_move == ChessBoard.BLACK_PAWN:
            new_to_move = ChessBoard.WHITE_PAWN
        else:
            new_to_move = ChessBoard.BLACK_PAWN
        new_position = Position(new_chessboard_matrix, new_to_move, move)
        return new_position


if __name__ == '__main__':
        chess_board = ChessBoard()
        game = Game(chess_board)
        mini_max = MinMax(game,None)

        #mini_max.generate_legal_moves(chess_board.chess_board,ChessBoard.BLACK_PAWN)
        mini_max.find_best_move_using_minimax()




