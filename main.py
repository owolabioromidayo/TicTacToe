import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        # Initial variables
        self.width = 800
        self.height = 800
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry(f"{self.width}x{self.height}")
        self.choices = list(range(0,9))
        self.centers = [[133,133],[400,133],[667,133],[133,400],[400,400],[667,400],[133,667],[400,667],[667,667]]
        self.player_turn = True
        self.game_over = False
        self.game = {}
        for i in range(9):
            self.game[i] = None



        self.root.bind('<Button-1>', self.on_click)

        self.build_gui()

        self.root.mainloop()


    def build_gui(self):
        #Create Board
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        
        #Create Lines
        self.linewidth = 3
        self.vert1 = self.canvas.create_line(self.width/3, 0,self.width/3 ,self.height, width=self.linewidth)
        self.vert2 = self.canvas.create_line(self.width*2/3, 0,self.width*2/3 ,self.height, width=self.linewidth)

        self.horiz1 = self.canvas.create_line(0,self.height/3,self.width, self.height/3, width=self.linewidth)
        self.horiz2 = self.canvas.create_line(0,self.height*2/3,self.width, self.height*2/3, width=self.linewidth)



    def on_click(self, event):
        if self.player_turn == True:
            x,y = event.x, event.y
            self.position = self.get_position(x,y)
            if self.position in self.choices:
                self.draw('X', self.position)
                self.choices.remove(self.position)
                self.game[self.position] = 'X'
                self.check_game_over()
                self.player_turn = False

                self.computer_choice()
        else:
            pass


    def computer_choice(self):
        self.choice = random.choice(self.choices)
        print(self.choice)
        self.draw('O',self.choice)
        self.choices.remove(self.choice)
        self.game[self.choice] = 'O'
        self.check_game_over()
        self.player_turn = True
        



    def draw(self, letter, position):
        x = self.centers[position][0]
        y = self.centers[position][1]
        self.canvas.create_text(x, y, text=letter, font=('Courier',44))


        
    def check_game_over(self):
        #Check rows
        
        for i in [0,3,6]:
            if self.game[i] == self.game[i+1] == self.game[i+2] and self.game[i] != None:
                self.alert(f"{self.game[i]} won")
                self.end_game()
                return

        for i in [0,1,2]:
            if self.game[i] == self.game[i+3] == self.game[i+6] and self.game[i] != None:
                self.alert(f"{self.game[i]} won")
                self.end_game()
                return

        if self.game[0] == self.game[4] == self.game[8] and self.game[0] != None:
            self.alert(f"{self.game[0]} won")
            self.end_game()
            return

        if self.game[2] == self.game[4] == self.game[6] and self.game[2] != None:
            self.alert(f"{self.game[2]} won")
            self.end_game()
            return


    



    



    def alert(self, message):
        messagebox.showinfo(title='Game Over',message=message)




    def end_game(self):
        self.root.destroy()



    def get_position(self, x, y):
        for i in range(1,4):
            _max = 267*i
            if x < _max:
                if y > 534:
                    return i+5
                elif y > 267:  
                    return i+2
                else:
                    return i-1
                




ttc = TicTacToe()


        

