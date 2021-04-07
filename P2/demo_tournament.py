"""Illustration of tournament.

Authors:
    Alejandro Bellogin <alejandro.bellogin@uam.es>

"""

from __future__ import annotations  # For Python 3.7

import numpy as np
import timeit



from game import Player, TwoPlayerGameState, TwoPlayerMatch
from heuristic import simple_evaluation_function
from tictactoe import TicTacToe
from tournament import StudentHeuristic, Tournament
from reversi import Reversi, from_array_to_dictionary_board, from_dictionary_to_array_board
import strategy

import studentheuristics


class Heuristic1(StudentHeuristic):

    def get_name(self) -> str:
        return "dummy"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        # Use an auxiliary function.
        return self.dummy(123)

    def dummy(self, n: int) -> int:
        return n + 4


class Heuristic2(StudentHeuristic):

    def get_name(self) -> str:
        return "random"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        return float(np.random.rand())


class Heuristic3(StudentHeuristic):

    def get_name(self) -> str:
        return "heuristic"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        return simple_evaluation_function(state)


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


tour = Tournament(max_depth=4, init_match=create_match)
# strats = {'opt1': [Heuristic1], 'opt2': [FusionHeuristic]}
strats = tour.load_strategies_from_folder(folder="studentheuristics", max_strat=3)


n = 5

scores, totals, names = tour.run(
    student_strategies=strats,
    increasing_depth=False,
    n_pairs=n,
    allow_selfmatch=True,
)

print(
    'Results for tournament where each game is repeated '
    + '%d=%dx2 times, alternating colors for each player' % (2 * n, n),
)

# print(totals)
# print(scores)

print('\ttotal:', end='')
for name1 in names:
    print('\t%s' % (name1), end='')
print()
for name1 in names:
    print('%s\t%d:' % (name1, totals[name1]), end='')
    for name2 in names:
        if name1 == name2:
            print('\t---', end='')
        else:
            print('\t%d' % (scores[name1][name2]), end='')
    print()

print (strategy.print_values())
