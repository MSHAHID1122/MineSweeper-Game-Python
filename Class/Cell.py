from tkinter import *
import random
import ctypes
import os
class CELL:

    cells = []
    Label = None
    Label_count = 36

    def __init__(self, x, y, is_mine=False):
        self.isMine = is_mine
        self.is_mine_candidate = False
        self.btn = None
        self.x = x
        self.y = y
        self.cells.append(self)
        self.is_opened = False

    def __repr__(self):
        return f'x={self.x}y={self.y}'

    def createbutton(self, location):
        botton = Button(location, width=15, height=5, bg="brown")
        botton.bind('<Button-1>', self.leftClick)
        botton.bind('<Button-3>', self.rightClick)
        self.btn = botton

    def leftClick(self, event):
        if CELL.Label_count < 10:
         ctypes.windll.user32.MessageBoxW(0, 'Congratulations You Won \n You are a MineShamer!!!', 'Victory', 0x40)
        if (self.isMine):
            self.showMine()
            result = ctypes.windll.user32.MessageBoxW(0, 'OOPS!! YOU CLICKED A MINE... GAME OVER\nDo you want to play again?', 'Game Over', 0x04 | 0x10)  # 0x04 for MB_YESNO, 0x10 for MB_ICONERROR
        
            if result == 6:  
                self.restartGame()  
            else:
                sys.exit() 
        elif (self.is_opened == False):
            self.showCell()

    def rightClick(self, event):
        if CELL.Label_count == 9:
            sys.windll.user32.MessageBox(3, 'Congratulations You Won \n You are a MineShamer!!!', 3)
        if not self.is_mine_candidate and not self.is_opened:
            self.btn.configure(bg="orange")
            self.is_mine_candidate = True

        else:
            self.btn.configure(bg='green')
            self.is_mine_candidate = False

    def showMine(self):
        self.btn.configure(bg="red")

    def showCell(self):

        mycell = self.get_surroundedcell()
        count = self.get_mines_num(mycell)

        if (self.is_opened == False):
            CELL.Label_count -= 1
        CELL.Label.configure(text=f"BOXES LEFT={CELL.Label_count}")
        self.btn.configure(bg='green')
        self.is_opened = True
        self.btn.configure(text=count)
        if (count == 0):
            for cell in mycell:
                if not cell.is_opened:
                    mycel = cell.get_surroundedcell()
                    cont = cell.get_mines_num(mycel)
                    cell.btn.configure(text=cont, bg="green")
                    CELL.Label_count -= 1
                    cell.is_opened = True

    @staticmethod
    def getcell(x: int, y: int):
        for cell in CELL.cells:
            if (cell.x == x and cell.y == y):
                return cell

    @staticmethod
    def createlabel(location):
        lbl = Label(
            location, text=f"BOXES LEFT={CELL.Label_count}", font=100, fg='black', bg="light green")
        CELL.Label = lbl

    def get_surroundedcell(self):
        mycell = [
            self.getcell(self.x, self.y+1),
            self.getcell(self.x-1, self.y+1),
            self.getcell(self.x-1, self.y),
            self.getcell(self.x-1, self.y-1),
            self.getcell(self.x, self.y-1),
            self.getcell(self.x+1, self.y-1),
            self.getcell(self.x+1, self.y),
            self.getcell(self.x+1, self.y+1)

        ]
        mycell = [cell for cell in mycell if cell is not None]
        return mycell

    @staticmethod
    def get_mines_num(mycell):
        count = 0
        for x in mycell:
            if (x.isMine == True):
                count += 1
        return count

    @staticmethod
    def rand_mine_gern():
        picked = random.sample(CELL.cells, 9)
        for pic in picked:
            pic.isMine = True

    def restartGame(self):
    # Function to restart the game
        self.resetBoard()  # Reset the board state
    # Re-generate mines for the new game
        CELL.rand_mine_gern()
    # Reset the label count to the initial value
        CELL.Label_count = 36
        CELL.Label.configure(text=f"BOXES LEFT={CELL.Label_count}")    
    def resetBoard(self):
        # Reset each cell to its initial state
        for cell in CELL.cells:
            cell.isMine = False  # Reset the mine status
            cell.is_mine_candidate = False  # Reset mine flag candidate
            cell.is_opened = False  # Set the cell as unopened
            cell.btn.configure(bg='brown', text='')  # Reset button appearance        
