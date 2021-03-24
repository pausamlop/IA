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



class FantasticHeuristic(StudentHeuristic):
  
  # devuelve el nombre de la heuristica
  def get_name(self) -> str:
    return "FantasticHeuristic"

  # funcion de evaluacion
  def evaluation_function (self, state: TwoPlayerGameState) -> float:

    aux = state.board
    puntos = 0

    if type(aux) != dict:
      board = from_array_to_dictionary_board(aux)

    for aux in board.values():
      if aux == state.player1.label:
        puntos += 1

    valor = len(state.game.generate_successors(state))

    if state.is_player_max(state.next_player):
      return 2*(puntos - valor)

    return 2*(puntos + valor)

  
    
#Devuelve el numero de esquinas por conquistar
class DestroyerHuristic(StudentHeuristic):

  def get_name(self) -> str:
    return "DestroyerHeuristic"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    black_corner_ini = 4
    white_corner_ini = 4
    corner = [(1, 1),(1, 8), (8, 1), (8,8)]

    black_corner = black_corner_ini - corner.count(state.player1.label)
    white_corner = white_corner_ini - corner.count(state.player2.label)


    siguiente_estado = state.game.generate_successors(state)

    aux_black = siguiente_estado.count(state.player1.label)
    aux_white = siguiente_estado.count(state.player2.label)
    
    black_corner_next_state = black_corner - aux_black
    white_corner_next_state = white_corner - aux_white

    if (state.is_player_max(state.next_player)==False) and (black_corner_next_state < black_corner):
      return black_corner_next_state

    if state.is_player_max(state.next_player) and (white_corner_next_state < white_corner):
      return white_corner_next_state

    return 4



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
