from random import randint

from chessboard import ChessBoard
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

    def print_current_turn(self):

        if self.turn == Player.AI:
            print ("It's the computer's turn!")
        elif self.turn == Player.HUMAN:
            print ("It's your turn!")

    def print_initial_message(self):
        print "You play with the white pawns"
        print "Computer plays with the black pawns"
        self.chessboard.print_chessboard()

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
                # TODO: MinMax Ai implementation
                pass

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
        move_tuples[0] = (int(moves[0][0]), moves[0][1])
        move_tuples[1] = (int(moves[1][0]), moves[1][1])
        return move_tuples

    def make_human_move(self, move):
        try:

            if move == None:
                raise Exception

            if not self.move_validator.is_move_valid(move[0], move[1]):
                raise Exception

        except:
            self.game_state = GameState.WRONG_MOVE
