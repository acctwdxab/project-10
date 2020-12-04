# Dan Wu
# 12/3/2020
# Write a class called BuildersGame that represents the board for a two-player game that is played on a 5x5 grid. During the game, each players' builders will move around the board and add levels to towers. The winner is the first one to move a builder on top of a 3-story tower.


class BuildersGame:
    """represents the board for a two-player game that is played on a 5x5 grid,
    with three private data members and two functions called get_current_state and make_move."""

    def __init__(self):
        """initializes the board to being empty, initializes the current_state to "UNFINISHED",
         and appropriately initializes any other data members."""
    
        self._board =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self._current_state = "UNFINISHED"
        self._turn = "x"
        self._xbuilder1 = None 
        self._xbuilder2 = None 
        self._obuilder1 = None 
        self._obuilder2 = None 
        self._count = 0 

    def get_current_state(self):
         """represent current status of the game"""
         return  self._current_state

    def _is_adjacent(self,x1,y1,x2,y2):
        """to check if coordinates are adjacent to each other"""
      
        if (x1==x2 and y1+1==y2) or(x1==x2 and y1-1==y2) or (x1+1 == x2 and y1-1 == y2) or(x1+1==x2 and y2==y1) or (x1+1==x2 and y1+1==y2)\
                or (x1-1==x2 and y1-1==y2) or (x1-1==x2 and y1==y2) or (x1-1==x2 and y1+1==y2) :

             return True

        else:

            return False



    def initial_placement(self,x1,y1,x2,y2,player):
        """takes five parameters: the row and column of each of the player's two builders,
        and either 'x' or 'o' to indicate the player who is placing builders.
        Rows and columns will be integers in the range 0-4."""

        if player == 'x' and self._turn!='o' and self._xbuilder1 is None and self._xbuilder2 is None: #make sure it has not been initialized
            self._turn = 'o'
            self._xbuilder1 = str(x1) + str(y1) #storing string values suppose intial placement is 1,2 for builder 1 then xb1 is "12"
            self._xbuilder2 = str(x2) + str(y2) # similar to above

        elif player == 'o' and self._turn!='x' and self._obuilder is None and self._obuilder is None:
            self._turn='x'
            str_of_builder1 = str(x1) + str(y1)
            str_of_builder2 = str(x2) + str(y2)
            #checking below if given initial placement is already occupied by the
            if self._xbuilder1 != str_of_builder1 and self._xbuilder1!=str_of_builder2 and self._xbuilder2!=str_of_builder1 and self._xbuilder2!=str_of_builder2:
                self._obuilder1 = str_of_builder1
                self._obuilder2 = str_of_builder2

            else:  #if builder square already occupied

                return  False



        else: # if o intitialized first

            return False
        return True #Don't forget return values

    def check_if_opponent_has_legal_move(self):
        """check if move is by the rule"""
        if self._turn == 'x':
            x1 = int(self._obuilder1[0])
            y1 = int(self._obuilder1[1])
            x2 = int(self._obuilder2[0])
            y2 = int(self._obuilder2(1))
            return check(x1,y1) or check(x2,y2)
        else:
            x1 = int(self._xbuilder1[0])
            y1 = int(self._xbuilder1[1])
            x2 = int(self._xbuilder2[0])
            y2 = int(self._xbuilder2(1))
            return check(x1,y1) or check(x2,y2)
        
    def check(self,x,y):
        level = self._board[x][y]
        if boundary_check(x-1,y-1) and self._board[x-1][y-1]-level<=1
          return True
        if boundary_check(x-1,y) and self._board[x-1][y]-level<=1
          return True
        if boundary_check(x-1,y+1) and self._board[x-1][y+1]-level<=1
          return True
        if boundary_check(x,y-1) and self._board[x][y-1]-level<=1
          return True
        if boundary_check(x,y+1) and self._board[x][y+1]-level<=1
          return True
        if boundary_check(x+1,y-1) and self._board[x+1][y-1]-level<=1
          return True
        if boundary_check(x+1,y) and self._board[x+1][y]-level<=1
          return True
        if boundary_check(x+1,y+1) and self._board[x+1][y+1]-level<=1
          return True
        return False

    def boundary_check(x,y):
        if x<0 or x>4 or y<0 or y>4:
            return False
        else
            return True
    
    def make_move(self,x1,y1,x2,y2,x3,y3):
        """if make move called before initial placement"""
        if self._xbuilder1 is None or self._xbuilder2 is None or self._obuilder1 is None or self._obuilder2 is None:# should use is None in Python maybe? Need to check
            return  False
        if self._current_state=='X_WON' or self._current_state=='O_WON':
            return  False
        str_builder = str(x1)+str(y1)
        str_destination = str(x2)+str(y2)
        str_level = str(x3) + str(y3)
        if self._count%2==0 and self._turn=='x':
            if str_builder!=self._xbuilder1 and str_builder!=self._xbuilder2:
                return  False
            if str_destination==self._xbuilder1 or str_destination == self._xbuilder2 or str_destination == self._obuilder1 or str_destination==self._obuilder2:
                return  False
            if not self._is_adjacent(x1,y1,x2,y2):#Maybe in python, we should use it in this way instead of ==False ? Need to check
                return False
            if  self._board[x2][y2] - self._board[x1][y1]>=2:
                return False
            if not self._is_adjacent(x2,y2,x3,y3):#Need to check
                return  Falss

            
            if str_builder == self._xbuilder1:
                self._xbuilder1 = str_destination
            elif str_builder == self._xbuilder2:
                self._xbuilder2 = str_destination

            self._board[x3][y3] += 1 #add 1 level at str_level
            if self._board[x3][y3]==4 or not self.check_if_opponent_has_legal_move():
               self._current_state = 'X_WON'
               return False
            else:
               self._turn='o'
               self._count+=1
               return  True
        
        elif self._count % 2 != 0 and self._turn == 'o':
            if str_builder != self._obuilder1 and str_builder != self._obuilder2:
                return False
            if str_destination == self._xbuilder1 or str_destination == self._xbuilder2 or str_destination == self._obuilder1 or str_destination == self._obuilder2:
                return False
            if self._is_adjacent(x1, y1, x2, y2) == False:
                return False
            if self._board[x2][y2] - self._board[x1][y1] >= 2:
                return False
            if self._is_adjacent(x2, y2, x3, y3) == False:
                return False

            if str_builder == self._obuilder1:
               self._obuilder1 = str_destination
            elseif str_builder == self._obuilder2:
               self._obuilder2 = str_destination
            self._board[x3][y3]+=1
            if self._board[x3][y3]==4 or not self.check_if_opponent_has_legal_move():
               self._current_state = 'O_WON'
               return False
            else:
               self._turn='x'
               self._count+=1
               return  True

        else:
            return  False
# game = BuildersGame()
# game.initial_placement(2,2,1,2,'x')
# game.initial_placement(0,1,4,2,'o')
# game.make_move(2,2,1,1,1,0)
# game.make_move(0,1,1,0,2,0)
# print(game.get_current_state())
