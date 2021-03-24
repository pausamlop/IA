"""Heuristicas para el torneo.

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
  """ Clase fantastic heuristic """
  
  def get_name(self) -> str:
    """ Nombre de la heuristica """
    return "FantasticHeuristic"

  def evaluation_function (self, state: TwoPlayerGameState) -> float:
    """ Funcion de evaluacion """

    aux = state.board
    puntos = 0

    # pasar el board a diccionario
    if type(aux) != dict:
      board = from_array_to_dictionary_board(aux)

    # contar el numero de fichas del jugador max
    for aux in board.values():
      if aux == state.player1.label:
        puntos += 1

    # numero de sucesores
    valor = len(state.game.generate_successors(state))

    # si es max
    if state.is_player_max(state.next_player):
      return 2*(puntos - valor)
      
    # si es min
    return 2*(puntos + valor)


# CASILLAS CONSOLIDADAS DE MAX
class NastyHeuristic(StudentHeuristic):
  """ Clase nasty heuristic """
  
  def get_name(self) -> str:
    """ Nombre de la heuristica """
    return "NastyHeuristic"

  def evaluation_function (self, state: TwoPlayerGameState) -> float:
    """ Funcion de evaluacion """

    total = 0
    height = state.board.height
    width = state.board.width
    square = dict()

    # comprobar que las esquinas estan ocupadas
    corner = [(1, 1),(1, width), (height, 1), (width,height)]
    if corner.count(state.player1.label)+corner.count(state.player2.label) == 0:
      return 0

    # PLAYER 1

    # rellenar las esquinas
    for i in corners:
      if board.get(i) == state.player1.label:
        square[i] = 1
      else:
        square[i] = 0

    # calcular el numero de iteraciones del bucle
    a, b, c, d = corner[0], corner[1], corner[2], corner[3]

    while (a[1] <= b[1]) and (a[0] <= c[0]):
      #filas
      for i in range(a[1],c[1]):
        #columnas
        for j in range(a[0],b[0]):
          square[(i,j)] = cons(square,i,j)

      #actualizar esquinas
      a[0] += 1
      a[1] += 1
      b[0] += 1
      b[1] -= 1
      c[0] -= 1
      c[1] += 1
      d[0] -= 1
      d[1] -= 1

  def cons(d: dict, i: int, j:int) -> int:   
    if 
    d[(i,j)] =  (cons(d,i,j-1) or cons(d,i,j+1)) and 
              (cons(d,i-1,j) or cons(d,i+1,j)) and 
              (cons(d,i-1,j+1) or cons(d,i+1,j-1)) and 
              (cons(d,i-1,j-1) or cons(d,i+1,j+1))


    # casillas consolidadas de max - casillas consolidadas de min
    return 0

      



  
    
#Devuelve el numero de esquinas por conquistar de cada jugador
class DestroyerHeuristic(StudentHeuristic):

  def get_name(self) -> str:
    return "DestroyerHeuristic"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    
    width = state.game.width
    height = state.game.height

    #Inicialmente aún no teien ninguna ficha en ninguna esquina
    black_corner_ini = 4
    white_corner_ini = 4

    corner = [(1, 1),(1, width), (height, 1), (width,height)]

    #Calculamos cuantas esquinas tienen con su ficha en cada momento
    black_corner = black_corner_ini - corner.count(state.player1.label)
    white_corner = white_corner_ini - corner.count(state.player2.label)


    siguiente_estado = state.game.generate_successors(state)
    
    #Calculaos cuantas esqinas conquistarían en el siguienet movimiento
    black_corner_next_state = black_corner - corner.count(siguiente_estado)
    white_corner_next_state = white_corner - corner.count(siguiente_estado)

    #En caso de conquistar otra esquina en el proximo movimiento se devuelve un nuevo valor de la heurística
    if (state.is_player_max(state.next_player)==False):
      return black_corner_next_state

    if state.is_player_max(state.next_player):
      return white_corner_next_state


class BombasticHeuristic(StudentHeuristic):

  width = state.game.width
  height = state.game.height

  def get_name(self) -> str:
    return "BombasticHeuristic"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    #Si el siguiente jugador es el max, mi actual enemigo es el max que es el plyer 1
    if state.is_player_max(state.next_player):
      enemmy=state.player1.label
    else:
      enemy=state.player2.label
    
    #Contamos los posibles siguientes movimientos
    for x in range(1, width + 1):
      for y in range(1, height + 1):
        if (x, y) not in state.board.keys() and 
        (((x+1,y) or  (x-1, y) or (x, y-1) or (x, y+1) or (x+1, y+1) or (x+1, y-1) or (x-1, y+1) or (x-1, y-1)) == enemy):
          result+=1
          
    return (width*length)-result


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
