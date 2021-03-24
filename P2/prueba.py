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
    width = state.game.width
    height = state.game.height

    #Inicialmente aún no teien ninguna ficha en ninguna esquina
    black_corner_ini = 4
    white_corner_ini = 4

    corner = [(1, 1),(1, width), (height, 1), (width,height)]


    black_corner = black_corner_ini - corner.count(state.player1.label)
    white_corner = white_corner_ini - corner.count(state.player2.label)


    siguiente_estado = state.game.generate_successors(state)

    black_corner_next_state = black_corner - corner.count(siguiente_estado)
    white_corner_next_state = white_corner - corner.count(siguiente_estado)

    if (state.is_player_max(state.next_player)==False):
      return black_corner_next_state

    if state.is_player_max(state.next_player):
      return white_corner_next_state

class BombasticHeuristic(StudentHeuristic):
  
  def get_name(self) -> str:
    return "BombasticHeuristic"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    width = state.game.width
    height = state.game.height
    aux = state.board
    result = 0

    if type(aux) != dict:
      board = from_array_to_dictionary_board(aux)

    #Si el siguiente jugador es el max, mi actual enemigo es el max que es el plyer 1
    if state.is_player_max(state.next_player):
      enemmy=state.player1.label
    else:
      enemy=state.player2.label
    
    #Contamos los posibles siguientes movimientos
    for x in range(1, width + 1):
      for y in range(1, height + 1):
        if (x, y) not in board.keys():
         if (((x+1,y) or  (x-1, y) or (x, y-1) or (x, y+1) or (x+1, y+1) or (x+1, y-1) or (x-1, y+1) or (x-1, y-1)) == enemy):
          result+=1
          
    return (width*height)-result



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
