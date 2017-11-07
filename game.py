from random import randint

from chessboard import ChessBoard


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
        self.player_piece = {Player.HUMAN : ChessBoard.WHITE_PAWN, Player.AI : ChessBoard.BLACK_PAWN}

    def print_current_turn(self):
        if self.game_state == GameState.WRONG_MOVE:
            print("Try again!")

        if self.turn == Player.AI:
            print ("It's the computer's turn!")
        elif self.turn == Player.HUMAN:
            print ("It's your turn!")

    def start_chess_game(self, first=Player.NONE):
        self.turn = first

        if self.turn == Player.NONE:
            self.turn = randint(Player.HUMAN, Player.AI)

        self.game_state = GameState.PLAYING
        self.chessboard.print_chessboard()

        while self.game_state != GameState.FINISHED:

            self.print_current_turn()

            self.chessboard.print_chessboard()

            if self.turn == Player.HUMAN:
                move = self.get_user_move()
                self.make_move(move)

            elif self.turn == Player.AI:
                #TODO: MinMax Ai implementation
                pass



            self.turn = (self.turn +1) % 2

    def get_user_move(self):
        move = raw_input("Enter your move: ")
        moves = move.split(" ")
        move_tuples = [(),()]
        move_tuples[0] = (int(moves[0][0]), moves[0][1])
        move_tuples[1] = (int(moves[1][0]), moves[1][1])
        return move_tuples

    def make_move(self,move):
        self.chessboard.move_piece(move[0], move[1])

