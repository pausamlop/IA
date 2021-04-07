"""Mide el tiempo de ejecucion de un demo_tournament.

Authors:
    Elena Cano <elena.canoc@estudiante.uam.es>
    Paula Samper <paula.samper@estudiante.uam.es>
"""

from __future__ import annotations  # For Python 3.7

import numpy as np
import timeit


from prueba import FusionHeuristic, EgoHeuristic, FantasticHeuristic
from game import Player, TwoPlayerGameState, TwoPlayerMatch
from heuristic import simple_evaluation_function
from tictactoe import TicTacToe
from tournament import StudentHeuristic, Tournament
from reversi import Reversi, from_array_to_dictionary_board, from_dictionary_to_array_board

mysetup = '''
from prueba import FusionHeuristic, EgoHeuristic, FantasticHeuristic
from game import Player, TwoPlayerGameState, TwoPlayerMatch
from heuristic import simple_evaluation_function
from tictactoe import TicTacToe
from tournament import StudentHeuristic, Tournament
from reversi import Reversi, from_array_to_dictionary_board, from_dictionary_to_array_board
'''






# code snippet whose execution time is to be measured 
mycode = ''' 
class Heuristic3(StudentHeuristic):

    def get_name(self) -> str:
        return "heuristic"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        return simple_evaluation_function(state)

class Heuristic1(StudentHeuristic):

    def get_name(self) -> str:
        return "dummy"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        # Use an auxiliary function.
        return self.dummy(123)

    def dummy(self, n: int) -> int:
        return n + 4



def create_match(player1: Player, player2: Player) -> TwoPlayerMatch:


    initial_player = player1


    initial_board = (
        ['..B.B..',
        '.WBBW..',
        'WBWBB..',
        '.W.WWW.',
        '.BBWBWB']
    )


    height = len(initial_board)
    width = len(initial_board[0])
    try:
        initial_board = from_array_to_dictionary_board(initial_board)
    except ValueError:
        raise ValueError('Wrong configuration of the board')
    #else:
        #print("Successfully initialised board from array")


    
    game = Reversi(
        player1=player1,
        player2=player2,
        height=5,
        width=7,
    )


    game_state = TwoPlayerGameState(
        game=game,
        board=initial_board,
        initial_player=initial_player,
    )

    return TwoPlayerMatch(game_state, max_sec_per_move=1000, gui=False)

tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Fusion1]}
n = 5
scores, totals, names = tour.run(
    student_strategies=strats,
    increasing_depth=False,
    n_pairs=n,
    allow_selfmatch=True,
)
'''

# timeit statement 
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 1)) 
