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




# CASILLAS CONSOLIDADAS DE MAX
class NastyHeuristic(StudentHeuristic):
  """ Clase nasty heuristic """
  
  def get_name(self) -> str:
    """ Nombre de la heuristica """
    return "NastyHeuristic"

  def evaluation_function (self, state: TwoPlayerGameState) -> float:
    """ Funcion de evaluacion """

    total = 0
    width = state.game.width
    height = state.game.height
    square1 = dict()
    square2 = dict()

    aux = state.board



    # pasar el board a diccionario
    if type(aux) != dict:
      board = from_array_to_dictionary_board(aux)


    # comprobar que las esquinas estan ocupadas
    corner = [(1, 1),(1, width), (height, 1), (width,height)]
    if corner.count(state.player1.label)+corner.count(state.player2.label) == 0:
      return 0


    # rellenar las esquinas
    for i in corners:
      if board.get(i) == state.player1.label:
        square1[i] = 1
        square2[i] = 0
      elif board.get(i) == state.player2.label:
        square2[i] = 1
        square1[i] = 0
      else:
        square2[i] = 0
        square1[i] = 0

    # calcular el numero de iteraciones del bucle
    a, b, c, d = corner[0], corner[1], corner[2], corner[3]

    while (a[1] <= b[1]) and (a[0] <= c[0]):
      #filas
      for i in range(a[1],c[1]):
        #columnas
        for j in range(a[0],b[0]):
          square1[(i,j)] = cons(square1,i,j)
          square2[(i,j)] = cons(square2,i,j)

      #actualizar esquinas
      a[0] += 1
      a[1] += 1
      b[0] += 1
      b[1] -= 1
      c[0] -= 1
      c[1] += 1
      d[0] -= 1
      d[1] -= 1

    a = sum(square1.values())
    b = sum(square2.values())


    return (a-b)+ len(state.game.generate_successors(state))

  def cons(d: dict, i: int, j:int) -> int:   
    if (i,j) in d:
      return d.get((i,j))

    a = cons(d,i,j-1) or cons(d,i,j+1)
    b = cons(d,i-1,j) or cons(d,i+1,j)
    c = cons(d,i-1,j+1) or cons(d,i+1,j-1)
    d = cons(d,i-1,j-1) or cons(d,i+1,j+1)

    return (a and b and c and d)




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
    else:
      board = aux

    for aux in board.values():
      if aux == state.player1.label:
        puntos += 1
      if aux == state.player2.label:
        puntos -= 1

    valor = len(state.game.generate_successors(state))

    return valor

  
    
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
    board = aux
    #Si el siguiente jugador es el max, mi actual enemigo es el max que es el plyer 1
    if state.is_player_max(state.next_player):
      enemmy=state.player1.label
    else:
      enemy=state.player2.label
    
    #Contamos los posibles siguientes movimientos
    for x in range(1, width + 1):
      for y in range(1, height + 1):
        if (x, y) not in board.keys():
         if (enemy == ((x+1,y) or  (x-1, y) or (x, y-1) or (x, y+1) or (x+1, y+1) or (x+1, y-1) or (x-1, y+1) or (x-1, y-1))):
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
