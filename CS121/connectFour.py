#Casey Gilray
#Assignment 10
#12/5/11

from random import choice

class board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.data = []
        
        for row in range(self.height):
            boardRow= []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]
            
    def __repr__(self):
        #prints out the row and columns of the baord
        s = '' #returned string
        for row in range(self.height):
            s += '|' #add spacer
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        
        #adds seperater to the string
        s += '--'*(self.width) + '-\n'
        
        #adds numbering to columns below seperater, wrapping back to zero
        #if there are more than 10 rows.
        for i in range(self.width):
            s += ' ' + str(i % 10)
        
        return s
        
    def addMove(self,col,ox):
        #find the first row in the given colum without an OX in it and add one
        for row in range (self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox
            
    def clear(self):
        #clears the object, making a clean new board
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '
        
    def allowMove(self,col):
        #Checks for a colum in range, and if it is not full
        if (0 <= col <= self.width):
            return self.isFull(col)
        else: return False
        
    def delMove(self,col):
        #Find the first row in the colum with an OX in it and remove it
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return
        
    def setBoard(self,moveString):
        #Sets up the board for a given number of turns in order
        nextCh = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col,nextCh)
            #Chcks for win after each symbol is placed
            if self.winFor(nextCh):
                print self
                print (nextCh + 'Wins')
                break
            elif self.full():
                print self
                print 'Catz game'
                break
            #Swaps to other symbol
            nextCh = oxSwap(nextCh)

    def isFull(self,col):
        #Checks to see if a colim is full for allowing move
        if self.data[0][col] == ' ':
            return True
        else: return False
    
    def winFor(self,ox):
        #checks for wins horizontally, vertically, and both diagonals
        #Check for horizontal wins
        for row in range(0,self.height):
            for col in range(0,self.width-3):
                if self.data[row][col] == ox and\
                   self.data[row][col+1] == ox and\
                   self.data[row][col+2] == ox and\
                   self.data[row][col+3] == ox:
                    return True
                
        #Check for vertical wins
        for row in range(0,self.height-3):
            for col in range(0,self.width):
                if self.data[row][col] == ox and\
                   self.data[row+1][col] == ox and\
                   self.data[row+2][col] == ox and\
                   self.data[row+3][col] == ox:
                    return True
                

        #Check for NE-SW wins
        for row in range(0,self.height-3):
            for col in range(3,self.width):
                if self.data[row][col] == ox and\
                   self.data[row+1][col-1] == ox and\
                   self.data[row+2][col-2] == ox and\
                   self.data[row+3][col-3] == ox:
                    return True
        #checks for NW-SE wins
        for row in range(0,self.height-3):
            for col in range(0,self.width-3):
                if self.data[row][col] == ox and\
                   self.data[row+1][col+1] == ox and\
                   self.data[row+2][col+2] == ox and\
                   self.data[row+3][col+3] == ox:
                    return True

    def full(self):
        #checks to see if the board is full
        for col in range(self.width):
            if self.allowMove(col) == True:
                return False
        return True 
    
            
    def getMove(self):
        #Gets a plays move, checking for errors that would cause a crash
        col = ''
        while True:
            ans = raw_input()
            #No entry error (entering values too quickly)
            if ans == '':
                print 'No Entry, Try again'
            #Non numeric input(letters or other calls)
            elif not(ans.isdigit()):
                print 'Not a number, Try again'
            else:
                #Change to integer and check for an allowed move on the board
                col = int(ans)
                if self.allowMove(col) == True:
                    return col
                else:
                    print 'Invalid Move, Try again'
                
    def hostGame(self):
        #plays a game of connectfour until a win is declared or until the board is full
        self.clear()
        nextCh = 'X'
        while True:
            print self
            
            print (nextCh +'\'s move:')
            #Gets players move 
            move = self.getMove()
            self.addMove(move,nextCh)
            if self.winFor(nextCh):
                print self
                print  (nextCh +' wins!')
                break
            elif self.full():
                print self
                print 'Catz Game'
                break
            #Sets for next players turn
            nextCh = oxSwap(nextCh)
                
    def playGameWith(self,aiPlayer):
        #Plays a game, using an AI players choice to make a move.
        self.clear()
        nextCh = 'X'
        while True:
            print self
            print (nextCh + '\'s move: ')
            #Uf its the AI players move, AI player picks its best move
            if aiPlayer.ox == nextCh:
                move = aiPlayer.nextMove(self)
            else:
                move = self.getMove()
            self.addMove(move, nextCh)
            if self.winFor(nextCh):
                print self
                print (nextCh + 'wins!')
                break
            elif self.full():
                print self
                print 'Catz Game'
                break
            #Sets for next players turn
            nextCh = oxSwap(nextCh)
            
class player:
        
    def __init__ (self,ox,ply,tieMode='left'):
            self.ox = ox
            self.ply = ply
            self.tieMode = tieMode
                               
    def nextMove(self,board):
        #Given a board, will choose its best move, using tieMode as a tie resoultion
        scores = self.scoresFor(board,self.ox,self.ply)
        #finds the best moves and picks the leftmost one
        topScores = lopScores(scores)
        if self.tieMode == 'left':
            pickMove = min(topScores)
        elif self.tieMode == 'right':
            pickMove = max(topScores)
        else:
            pickMove = randomPick(topScores)
        print pickMove[1]
        return(pickMove[1])
    
    def scoresFor(self,board,ox,ply):
        #Scores a board for the computer player recursivly
        scores = []
        for cols in range(0,board.width):
            if board.allowMove(cols):
                #Adds the move and checks for a win
                board.addMove(cols,ox)
                if board.winFor(ox): 
                    scores += [(100.0,cols)] #adds win score to list in the form of a tuple
                else: 
                    if ply == 0 :
                        scores += [(50.0,cols)]
                    else:
                        #Recursion, scores board in terms of the opponent, getting the min of those scores, and reversing them.
                        themscore = self.scoresFor(board,oxSwap(ox),(ply-1))
                        themscore = max(themscore)
                        scores +=[(((100-themscore[0])*.99),cols)]
                #Deletes added move
                board.delMove(cols)
            else: scores += [(-1.0,cols)]
        return scores
        
def oxSwap(ox):
        if ox == 'X': ox = 'O'
        else: ox = 'X'
        return ox
    
def lopScores(scores):
    returnScores = []
    #Finds the maximum score, then returns a list of all scores with the same value
    maxScore = max(scores)[0]
    for a in range(0,len(scores)):
        if scores[a][0] == maxScore:
            returnScores += [scores[a]]
    return returnScores

def randomPick(scores):
    a = choice(range(0,(len(scores))))
    return scores[a]
        
        
b = board(7,6)
ai = player('O',5,'random')
print 'Type b.hostgame() to play a new game'
b.playGameWith(ai)