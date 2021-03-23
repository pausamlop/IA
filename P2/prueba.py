import time
from game import (
    TwoPlayerGameState,
    Player,
)
from tournament import (
    StudentHeuristic,
)
from reversi import (
    Reversi,
    from_array_to_dictionary_board,
    from_dictionary_to_array_board,
)



class FirstHeuristic(StudentHeuristic):
  
  # devuelve el nombre de la heuristica
  def get_name(self) -> str:
    return "FirstHeuristic"

  # funcion de evaluacion
  def evaluation_function (self, state: TwoPlayerGameState) -> float:

    aux = state.board
    puntos = 0

    if type(aux) != dict:
      board = from_array_to_dictionary_board(aux)

    for aux in board.values():
      if aux == state.next_player.label:
        puntos += 1

    valor = len(state.game.generate_successors(state))

    if state.is_player_max(state.next_player):
      return 2*(puntos - valor)

    return 2*(puntos + valor)
    

# class destroyerHuristic(StudenHeuristic):
#   def get_name(self) -> str:
#     return "destryerheuristic"

#   def evaluation_function(self, state: TwoPlayerGameState) -> float:
#     # let's use an auxiliary function
#     aux = self.dummy(123)
#     return aux

#   def dummy(self, n: int) -> int:
#     return n + 1



class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "solution1"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    # let's use an auxiliary function
    aux = self.dummy(123)
    return aux

  def dummy(self, n: int) -> int:
    return n + 1

class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "solution2"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    print("sleeping")
    time.sleep(3)
    print("awake")
    return 2
