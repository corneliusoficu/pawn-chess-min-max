import copy

from chessboard import ChessBoard


class Position:
    def __init__(self, chessboard, to_move, current_move=None, has_eaten_enemy=0):
        self.to_move = to_move
        self.chessboard = copy.deepcopy(chessboard)
        self.current_move = current_move
        self.has_eaten_enemy = has_eaten_enemy


class MinMax:
    TREE_HEIGHT = 4

    def __init__(self, game, move_validator):

        self.chessboard = game.chessboard.chess_board
        self.game = game
        self.move_validator = game.move_validator
        self.game_engine = game.game_engine

    def find_best_move_using_minimax(self):
        position = Position(self.chessboard, ChessBoard.BLACK_PAWN)
        bestscore, bestmove = self.minimax(position, MinMax.TREE_HEIGHT)
        return bestmove

    def minimax(self, position, depth):
        if depth == 0 or \
                self.game_engine.is_draw(position.chessboard) or \
                self.game_engine.is_win(position.chessboard):
            return (self.evaluate_position(position), None)
        else:
            if position.to_move == ChessBoard.BLACK_PAWN:
                best_score = -float("inf")
                best_move = None
                valid_moves = self.game_engine.generate_random_moves(position.chessboard, position.to_move)
                for move in valid_moves:
                    new_position = self.make_move_for_position(position, move)
                    score, mini_max_move = self.minimax(new_position, depth - 1)
                    if score > best_score:
                        best_score = score
                        best_move = move
                return (best_score, best_move)
            else:
                best_score = float("inf")
                best_move = None
                valid_moves = self.game_engine.generate_random_moves(position.chessboard, position.to_move)
                for move in valid_moves:
                    new_position = self.make_move_for_position(position, move)
                    score, mini_max_move = self.minimax(new_position, depth - 1)

                    if score < best_score:
                        best_score = score
                        best_move = move
                return (best_score, best_move)

    def evaluate_position(self, position):

        if self.game_engine.is_win(position.chessboard):
            return 5

        elif self.game_engine.is_draw(position.chessboard):
            return 4

        elif position.has_eaten_enemy == 1:
            return 3

        else:

            from_row = position.current_move[0][0]
            to_row = position.current_move[1][0]

            row_diff = abs(to_row - from_row)

            if row_diff == 2:
                return 2
            elif row_diff == 1:
                return 1

    def make_move_for_position(self, position, move):

        new_chessboard_matrix = copy.deepcopy(position.chessboard)
        has_eaten_enemy = ChessBoard.move_piece(new_chessboard_matrix, move[0], move[1])

        if position.to_move == ChessBoard.BLACK_PAWN:
            new_to_move = ChessBoard.WHITE_PAWN
        else:
            new_to_move = ChessBoard.BLACK_PAWN

        new_position = Position(new_chessboard_matrix, new_to_move, move, has_eaten_enemy)
        return new_position



