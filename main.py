import random, sys, time
import tkinter as tk
import minimax_helpers as minimax

from tkinter import messagebox
from math import inf as infinity

class TicTacToe:
    def __init__(self, size, cell_size, choice_mechanism='minmax'):
        # Initial game state
        self.size, self.cell_size = size, cell_size
        self.choice_mechanism = choice_mechanism
        self.choices = set(range(0, self.size**2))  # board postions
        self.player_turn = True

        self.game = [[' ' for j in range(self.size)]for i in range(self.size)]

        self.build()

    def gen_centers(self):

        self.centers_1d = [
            self.cell_size/2+(self.cell_size*i)for i in range(self.size)
        ]

        self.centers = [
            [x, y]for x in self.centers_1d for y in self.centers_1d
        ]

    def gen_lines(self, linewidth):
        # Doesnt include first and last, only ones necceaasry for line to cross
        self.edges = [self.cell_size*i for i in range(1, self.size)]

        for edge in self.edges:
            self.canvas.create_line(
                edge, 0, edge, self.height, width=linewidth
            )  # vert lines

            self.canvas.create_line(
                0, edge, self.width, edge, width=linewidth
            )  # horiz lines

    def build(self):
        self.width = self.height = self.size*self.cell_size

        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.bind('<Button-1>', self.on_click)

        self.gen_centers()

        # Create Board
        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.gen_lines(7)
        # self.computer_choice() #computer first
        self.root.mainloop()

    def on_click(self, event):
        if self.player_turn:
            pos, x_pos, y_pos = self.get_pos(event.x, event.y)
            if pos in self.choices:
                self.draw('X', pos)
                self.choices.remove(pos)
                self.game[y_pos][x_pos] = 'X'
                self.player_turn = False
                self.check_game_over()
                self.computer_choice()

    def computer_choice(self):
        if self.choice_mechanism == 'minmax':
            choice = minimax.alphabeta(self.game, 'O', -infinity, infinity )['index']

        else:
            choice = random.sample(self.choices, 1)[0]
        
        y = choice // self.size
        x = choice - (y * self.size)

        print(choice)
        self.draw('O', choice)
        self.choices.remove(choice)
        self.game[y][x] = 'O'
        self.check_game_over()
        self.player_turn = True


    def draw(self, letter, pos):
        x, y = self.centers[pos][1], self.centers[pos][0]
        color = 'blue' if letter == 'O' else 'red'
        self.canvas.create_text(
            x, y, text=letter, font=('Times', 44), fill=color)

    def check_game_over(self):

        # Check rows and cols in one loop (faster)
        diag1, diag2 = [], []
        for i, row in enumerate(self.game):

            # Check row
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return self.end_game(f"{row[0]} won")

            # check col
            col = [row[i] for row in self.game]
            if col.count(col[0]) == len(col) and col[0] != ' ':
                return self.end_game(f"{col[0]} won")

            diag1.append(self.game[i][i])
            diag2.append(self.game[i][len(self.game)-1-i])

        if diag1.count(diag1[0]) == len(diag1) and diag1[0] != ' ':
            return self.end_game(f"{diag1[0]} won")

        if diag2.count(diag2[0]) == len(diag2) and diag2[0] != ' ':
            return self.end_game(f"{diag2[0]} won")

        # Check draw
        count = 0
        for i in self.game:
            for j in i:
                if j != ' ':
                    count += 1

        if count == self.size**2:
            return self.end_game("Draw!")

    def end_game(self, message):
        messagebox.showinfo(title='Game Over', message=message)
        self.root.destroy()
        sys.exit()

    def get_pos(self, x, y):
        """returns board position based on x and y coords"""
        x_pos, y_pos = 0, 0
        for edge in self.edges:
            x_pos = x_pos+1 if x > edge else x_pos
            y_pos = y_pos+1 if y > edge else y_pos

        pos = y_pos*self.size + x_pos
        return pos, x_pos, y_pos


if __name__ == "__main__":
    ttc = TicTacToe(4, 100, 'random')
