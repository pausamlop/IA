"""Heuristicas para reversi.

Authors:
    Elena Cano <elena.canoc@estudiante.uam.es>
    Paula Samper <paula.samper@estudiante.uam.es>

"""


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


    valor = len(state.game.generate_successors(state))

    return valor




#Devuelve el numero de fichas de cada jugador que faltan para conquistar todo el tablero
class EgoHeuristic(StudentHeuristic):
  
  #devuelve el nombre de la heuristica
  def get_name(self) -> str:
    return "EgoHeuristic"

  # funcion de evaluacion
  def evaluation_function (self, state: TwoPlayerGameState) -> float:

    aux = state.board
    puntosMax = 0
    puntosMin = 0
    total = state.game.width * state.game.height
    

    if type(aux) != dict:
      board = from_array_to_dictionary_board(aux)
    else:
      board = aux

    for aux in board.values():
      if aux == state.player1.label:
        puntosMax += 1
      if aux == state.player2.label:
        puntosMin += 1

    if state.is_player_max(state.next_player):
      return total - puntosMin

    return total - puntosMax


class FusionHeuristic(StudentHeuristic):

  #devuelve el nombre de la heuristica
  def get_name(self) -> str:
    return "FusionHeuristic"

  # funcion de evaluacion
  def evaluation_function (self, state: TwoPlayerGameState) -> float:
    aux1 = FantasticHeuristic.evaluation_function(self, state)
    aux2 = EgoHeuristic.evaluation_function(self, state)

    if state.is_player_max(state.next_player):
      return min(aux1,aux2)
    return max(aux1, aux2)
