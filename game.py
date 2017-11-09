from random import randint

from chessboard import ChessBoard
from game_engine import GameEngine
from minmax import MinMax
from move_validator import MoveValidator


class Player():
    HUMAN = 0
    AI = 1
    NONE = 2


class GameState():
    PLAYING = 0
    FINISHED = 1
    WRONG_MOVE = 2


class Game:
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.player_piece = {Player.HUMAN: ChessBoard.WHITE_PAWN, Player.AI: ChessBoard.BLACK_PAWN}
        self.move_validator = MoveValidator(self)
        self.turn = Player.HUMAN
        self.was_last_move_a_two_step_move = True
        self.position_of_two_steps_pawn = (4,'C')
        self.game_engine = GameEngine(self)
        self.mini_max = MinMax(self, self.move_validator)

    def print_current_turn(self):

        if self.turn == Player.AI:
            print ("It's the computer's turn!")
        elif self.turn == Player.HUMAN:
            print ("It's your turn!")

    def print_initial_message(self):
        print "You play with the white pawns"
        print "Computer plays with the black pawns"

    def start_chess_game(self, first=Player.NONE):
        self.turn = first

        if self.turn == Player.NONE:
            self.turn = randint(Player.HUMAN, Player.AI)

        self.game_state = GameState.PLAYING

        self.print_initial_message()

        while self.game_state != GameState.FINISHED:

            self.print_current_turn()

            self.chessboard.print_chessboard()

            if self.turn == Player.HUMAN:
                move = self.get_user_move()
                self.make_human_move(move)

            elif self.turn == Player.AI:
                best_ai_move = self.mini_max.find_best_move_using_minimax()
                ChessBoard.move_piece(self.chessboard.chess_board, best_ai_move[0], best_ai_move[1])


            if self.game_state != GameState.WRONG_MOVE:
                self.turn = (self.turn + 1) % 2
            else:
                print "Enter a correct move!"

    def get_user_move(self):
        move = raw_input("Enter your move: ")
        if len(move) != 5:
            print "Wrong input format for move!"
            return None
        moves = move.split(" ")
        move_tuples = [(), ()]
        move_tuples[0] = (int(moves[0][0]), MoveValidator.convert_character_to_integer(moves[0][1]))
        move_tuples[1] = (int(moves[1][0]), MoveValidator.convert_character_to_integer(moves[1][1]))
        return move_tuples

    def make_human_move(self, move):
        try:

            if move == None:
                raise Exception

            if not self.move_validator.is_move_valid(self.chessboard.chess_board, move[0], move[1], ChessBoard.WHITE_PAWN):
                raise Exception

            ChessBoard.move_piece(self.chessboard.chess_board, move[0], move[1])

            self.game_state = GameState.PLAYING

        except:
            self.game_state = GameState.WRONG_MOVE
