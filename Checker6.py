from tkinter import *
from tkinter import messagebox
class CheckersSquare(Canvas):
    '''displays a square in the Checkers game'''
 
    def __init__(self,master,r,c,color):
        '''CheckersSquare(master,r,c)
        creates a new Checker square at coordinate (r,c)'''
        # create and place the widget
        
        Canvas.__init__(self,master,width=50,height=50,bg='dark green')
        self.grid(row=r,column=c)
        self['highlightbackground'] = 'dark green'
        # set the attributes
        self.isKing = False
        self.position = (r,c)
        self.color = color
        if self.color != None:
            self.create_oval(10,10,44,44,fill=self.color) 
        if self.isKing == True:
            self.create_text(28,28,text='♕',font=('Times',24))
        
            
        # bind button click to placing a piece
        self.bind('<Button>',master.get_click)
 
    def get_position(self):
        '''CheckersSquare.get_position() -> (int,int)
        returns (row,column) of square'''
        return self.position
    def is_king(self):
        return self.isKing
    def make_oval_color(self,color,isking):
        '''CheckersSquare.make_color(color)
        changes color of piece on square to specified color'''
        ovalList = self.find_all()  # remove existing piece
        for oval in ovalList:
            self.delete(oval)
        self.create_oval(10,10,44,44,fill=color)
        if isking == True:
            self.create_text(28,28,text='♕',font=('Times',24))
            self.isKing = True
        if color == 'white':
            colorPlayer = 1
        else:
            colorPlayer = 0
        self.master.board[self.get_position()] = colorPlayer
    def change_blank(self):
        self['bg']='blanched almond'
        self['highlightbackground'] = 'blanched almond'
        self['state']=DISABLED
    def erase_oval(self):
        ovalList = self.find_all()  # remove existing piece
        for oval in ovalList:
            self.delete(oval)
        self.master.board[self.get_position()] = None
    def make_king(self):
        self.isKing = True
        self.create_text(28,28,text='♕',font=('Times',24))
    def delete_king(self):
        self.isKing = False
        
class CheckersGame(Frame):
    '''represents a game of Checkers'''
    def __init__(self,master):
        '''CheckersGame(master)
        creates a new Checkers game'''
        # initialize the Frame
        Frame.__init__(self,master,bg='white')
        self.grid()
        self.board = {}  # dict to store position
        self.startReds = []
        self.startWhites = []
        self.currentClicked = []
        self.goToThis = []
        self.currentPlayer = 0
        self.nextPlayer = 0
        self.moveInProgress = False
        # create opening position
        for i in range(1,8,2):
            for n in range(0,3,2):
                self.startReds.append((n,i))
        for i in range(0,8,2):
            for n in range(1,3,2):
                self.startReds.append((n,i))
        for i in range(0,8,2):
            for n in range(5,8,2):
                self.startWhites.append((n,i))
                
        for i in range(1,8,2):
            for n in range(6,8,2):
                self.startWhites.append((n,i))
        for row in range(8):
            for column in range(8):
                coords = (row,column)
                if coords in self.startWhites:
                    self.board[coords] = 1  # player 1
                elif coords in self.startReds:
                    self.board[coords] = 0  # player 0
                else:
                    self.board[coords] = None  # empty
        self.squares = {}
        self.newcoordList = []
        self.colors = ('red','white')  # players' colors
        for row in range(8):
            for column in range(8):
                rc = (row,column)
                if self.board[rc]==0:
                    color = 'red'
                elif self.board[rc]==1:
                    color = 'white'
                else:
                    color = None
                self.squares[rc] = CheckersSquare(self,row,column,color)
        for row in range(1,8,2):
            for column in range(1,8,2):
                coord = (row,column)
                self.squares[coord].change_blank()
        for row in range(0,8,2):
            for column in range(0,8,2):
                coord = (row,column)
                self.squares[coord].change_blank()
        self.coordList = []
        for row in range(8):
            for col in range(8):
                if self.squares[(row,col)]['highlightbackground'] != 'blanched almond':
                    self.newcoordList.append((row,col))
        self.turnSquare = CheckersSquare(self,9,3,None)
        self.turnSquare.make_oval_color(self.colors[self.currentPlayer],False)
        self.turnSquare.unbind('<Button>')
        self.scoreLabel = Label(self,text='It is '+str(self.colors[self.currentPlayer])+ "'s turn",font=('Comic Sans MS',12) )
        self.scoreLabel.grid(row=9,column=0,columnspan=3)
    def available_moves(self,coords):
        '''get a list of the coords it can move to '''
        row = coords[0]
        col = coords[1]
        if self.squares[coords].is_king() is True:
            kingList = []
            jumpkingList = []
            for rows in range(row - 1, row + 2):  # This helped so much! I'm glad you gave me a suggestion to use a loop in Minesweeper
                for columns in range(col - 1, col + 2): #Is this right, do kings get to move any direction?
                        if (rows,columns) in self.newcoordList:
                            if self.board[(rows,columns)] == None:
                                kingList.append((rows,columns))
            for newcoord in [(row+1,col-1),(row+1,col+1)]:
                if newcoord in self.newcoordList and self.board[newcoord] != None:
                    if newcoord[1] < coords[1] and self.board[newcoord] == 1-self.currentPlayer:
                        if (newcoord[0]+1,newcoord[1]-1) in self.newcoordList and self.board[(newcoord[0]+1,newcoord[1]-1)] == None:
                            jumpkingList.append((newcoord[0]+1,newcoord[1]-1))
                    if newcoord[1] > coords[1] and self.board[newcoord] == 1-self.currentPlayer:
                        if (newcoord[0]+1,newcoord[1]+1) in self.newcoordList and self.board[(newcoord[0]+1,newcoord[1]+1)] == None:
                            jumpkingList.append((newcoord[0]+1,newcoord[1]+1))
            for new in [(row-1,col-1),(row-1,col+1)]:
                if new in self.newcoordList and self.board[new] != None:
                    if new[1] < coords[1] and self.board[new] == 1-self.currentPlayer:
                        if (new[0]-1,new[1]-1) in self.newcoordList and self.board[(new[0]-1,new[1]-1)] == None:
                            jumpkingList.append((new[0]-1,new[1]-1))
                    if new[1] > coords[1] and self.board[new] == 1-self.currentPlayer:
                        if (new[0]-1,new[1]+1) in self.newcoordList and self.board[(new[0]-1,new[1]+1)] == None:
                            jumpkingList.append((new[0]-1,new[1]+1))
            if len(jumpkingList) > 0:
                return (jumpkingList,True)
            return (kingList, False)
        elif self.currentPlayer == 0:
            redMoves = []
            redjumpMoves = []
            for newcoord in [(row+1,col-1),(row+1,col+1)]:
                if newcoord in self.newcoordList and self.board[newcoord] == None:
                    redMoves.append(newcoord)
                if newcoord in self.newcoordList and self.board[newcoord] != None:
                    if newcoord[1] < coords[1] and self.board[newcoord] == 1:
                        if (newcoord[0]+1,newcoord[1]-1) in self.newcoordList and self.board[(newcoord[0]+1,newcoord[1]-1)] == None:
                            redjumpMoves.append((newcoord[0]+1,newcoord[1]-1))
                    if newcoord[1] > coords[1] and self.board[newcoord] == 1:
                        if (newcoord[0]+1,newcoord[1]+1) in self.newcoordList and self.board[(newcoord[0]+1,newcoord[1]+1)] == None:
                            redjumpMoves.append((newcoord[0]+1,newcoord[1]+1))
            endList = (redMoves,False)
            if len(redjumpMoves) > 0:
                endList = (redjumpMoves,True)
        elif self.currentPlayer==1:
            whiteMoves = []
            whitejumpMoves = []
            for new in [(row-1,col-1),(row-1,col+1)]:
                if new in self.newcoordList and self.board[new] == None:
                    whiteMoves.append(new)
                if new in self.newcoordList and self.board[new] != None:
                    if new[1] < coords[1] and self.board[new] == 0:
                        if (new[0]-1,new[1]-1) in self.newcoordList and self.board[(new[0]-1,new[1]-1)] == None:
                            whitejumpMoves.append((new[0]-1,new[1]-1))
                    if new[1] > coords[1] and self.board[new] == 0:
                        if (new[0]-1,new[1]+1) in self.newcoordList and self.board[(new[0]-1,new[1]+1)] == None:
                            whitejumpMoves.append((new[0]-1,new[1]+1))
            endList = (whiteMoves, False)
            if len(whitejumpMoves) > 0:
                endList = (whitejumpMoves,True)
        return endList
    def check_lose(self):
        loseGame = True
        for square in self.squares:
            if self.currentPlayer == self.board[self.squares[square].get_position()]:
                if len(self.available_moves(self.squares[square].get_position())[0]) >0:
                    loseGame = False
        return loseGame
    def end_game(self):
        messagebox.showerror('Checkers',str(self.colors[1-self.currentPlayer])+", you won!",parent=self)
        endmessage = Canvas(self,width=400,height=400,bg='dark green')
        endmessage.grid(row=0,column=0,columnspan=9,rowspan=9)
        endmessage.create_text(200,180,text='Have a good day!',font=('Times',42))
    def get_click(self,event):
        '''CheckersGame.get_click(event)
        event handler for mouse click
        gets click data and makes the move'''
        mustJump = False
        coords = event.widget.get_position()
        coord = coords
        square = self.squares[coords]
        if self.moveInProgress is False and self.board[coords] == self.currentPlayer:
            for picksquare in self.squares:
                if self.board[self.squares[picksquare].get_position()] == self.currentPlayer:
                    if self.available_moves(self.squares[picksquare].get_position())[1] == True:
                        mustJump = True
            if len(self.available_moves(coords)[0]) > 0:
                if mustJump == False: 
                    moves = self.available_moves(coords)[0]
                    for move in moves:
                        self.squares[move]['highlightbackground']='blue' #show the available moves
                    self.currentClicked = square
                    self.moveInProgress = True
                    square['highlightbackground'] = 'black'
                if mustJump == True:
                    while self.available_moves(coord)[1] is True and self.available_moves(coord)[0]!=[]:
                        
                        moves = self.available_moves(coord)[0]
                        for move in moves:
                            self.squares[move]['highlightbackground']='blue'
                        coord = moves[0]
                        
                        self.currentClicked = square
                        self.moveInProgress = True
                        square['highlightbackground'] = 'black'
        else:
            if square['highlightbackground']== 'blue':
                for eachSquare in self.available_moves(self.currentClicked.get_position())[0]:
                    self.squares[eachSquare]['highlightbackground'] = 'dark green'
                    if eachSquare is not square.get_position():
                        bluesquare = eachSquare
                square.make_oval_color(self.colors[self.currentPlayer],self.currentClicked.is_king())
                self.currentClicked.erase_oval()
                self.board[self.currentClicked] = None
                self.currentClicked['highlightbackground'] = 'dark green'
                square['highlightbackground'] = 'dark green'
                self.moveInProgress = False
                changecoord = coords
                if self.currentClicked.get_position()[1] + 1 < square.get_position()[1]: # Erase the checkers that are jumped
                    if self.currentClicked.get_position()[0] + 1 < square.get_position()[0]:
                        eraseThis = (square.get_position()[0]-1,square.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]+1,self.currentClicked.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                    else:
                        eraseThis = (square.get_position()[0]+1,square.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]-1,self.currentClicked.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                        
                if self.currentClicked.get_position()[1]-1 >  square.get_position()[1]:
                    if self.currentClicked.get_position()[0]-1 > square.get_position()[0]:
                        eraseThis = (square.get_position()[0]+1,square.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]-1,self.currentClicked.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                    else:
                        eraseThis = (square.get_position()[0]-1,square.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]+1,self.currentClicked.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                elif self.currentClicked.get_position()[0]-2 > square.get_position()[0] and self.currentClicked.get_position()[1] == square.get_position()[1]:########################
                    if bluesquare[1] < square.get_position()[1] and bluesquare[1] < self.currentClicked.get_position()[1]:
                        eraseThis = (square.get_position()[0]+1,square.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]-1,self.currentClicked.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                    elif bluesquare[1] > square.get_position()[1] and bluesquare[1] > self.currentClicked.get_position()[1]:
                        eraseThis = (square.get_position()[0]+1,square.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]-1,self.currentClicked.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                elif self.currentClicked.get_position()[0] < square.get_position()[0]-2 and self.currentClicked.get_position()[1] == square.get_position()[1]:########################
                    if bluesquare[1] < square.get_position()[1] and bluesquare[1] < self.currentClicked.get_position()[1]:
                        eraseThis = (square.get_position()[0]-1,square.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]+1,self.currentClicked.get_position()[1]-1)
                        self.squares[eraseThis].erase_oval()
                    elif bluesquare[1] > square.get_position()[1] and bluesquare[1] > self.currentClicked.get_position()[1]:
                        eraseThis = (square.get_position()[0]-1,square.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                        eraseThis = (self.currentClicked.get_position()[0]+1,self.currentClicked.get_position()[1]+1)
                        self.squares[eraseThis].erase_oval()
                if square.get_position()[1] in [1,3,5,7] and square.get_position()[0] == 0 and self.currentPlayer == 1:
                    square.make_king()
                if square.get_position()[1] in [0,2,4,6] and square.get_position()[0] == 7 and self.currentPlayer == 0:
                    square.make_king()
                self.currentPlayer = 1- self.currentPlayer
                self.turnSquare.make_oval_color(self.colors[self.currentPlayer],False)
                self.scoreLabel['text']='It is '+str(self.colors[self.currentPlayer])+ "'s turn"
                if self.check_lose() == True:
                    self.end_game()
                if self.moveInProgress is False and self.board[coords] == self.currentPlayer:
                    for picksquare in self.squares:
                        if self.board[self.squares[picksquare].get_position()] == self.currentPlayer:
                            if self.available_moves(self.squares[picksquare].get_position())[0] < 1:
                                self.end_game()
            else:
                if square['highlightbackground']== 'blanched almond':
                    pass
                elif self.board[coords] != self.currentPlayer:
                    pass
                else:
                    square['highlightbackground'] = 'dark green'
                    self.currentClicked['highlightbackground'] = 'dark green'
                    self.moveInProgress = False
                    for eachSquare in self.available_moves(self.currentClicked.get_position())[0]:
                        self.squares[eachSquare]['highlightbackground'] = 'dark green'
def play_checker():
    '''play_checker()
    starts a new game of Checkers'''
    root = Tk()
    root.title('Checkers')
    Checker = CheckersGame(root)
    Checker.mainloop()
play_checker()
