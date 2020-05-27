import random
import itertools
import tkinter as tk
from tkinter import messagebox
import numpy as np


class TicTacToe:
    def __init__(self, size, cell_size):
        # Initial game state
        self.size, self.cell_size = size, cell_size
        self.choices = set(range(0, self.size**2))  # board postions
        self.player_turn = True
        self.game_over = False

        # Logical board build
        self.game = [{i: None} for i in range(self.size**2)]
        # Groups list of dicts into groups of 3
        iters = [iter(self.game)] * self.size
        # iters = list(map(lambda x: list(x), iters))

        # print(iters)
        self.game = list(zip(*iters))
        self.game = list(map(lambda x: list(x), self.game))
        print(self.game)

        # self._test_space()
        self.build()

    def gen_centers(self):
        # x_edges = np.uniform(0, self.size*100, self.size)
        # edges = [100*i for i in range(self.size+1)]
        # print(edges)
        # centers = []
        # for idx, i in enumerate(edges[:-1]):
        #     new_center = (i + edges[idx+1])/2
        #     centers.append(new_center)

        self.centers_1d = [self.cell_size/2+(self.cell_size*i)
                           for i in range(self.size)]

        # print(centers)
        # pairs = []
        # for i in centers:
        #     new_row = [[i, j] for j in centers]
        #     for pos in new_row:
        #         pairs.append(pos)

        self.centers = [[x, y]
                        for x in self.centers_1d for y in self.centers_1d]

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

        # self.vert1 = self.canvas.create_line(
        #     self.width/3, 0, self.width/3, self.height, width=linewidth)
        # self.vert2 = self.canvas.create_line(
        #     self.width*2/3, 0, self.width*2/3, self.height, width=linewidth)

        # self.horiz1 = self.canvas.create_line(
        #     0, self.height/3, self.width, self.height/3, width=linewidth)
        # self.horiz2 = self.canvas.create_line(
        #     0, self.height*2/3, self.width, self.height*2/3, width=linewidth)

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
        self.root.mainloop()

    def on_click(self, event):
        if self.player_turn:
            pos, x_pos, y_pos = self.get_pos(event.x, event.y)
            if pos in self.choices:
                self.draw('X', pos)
                self.choices.remove(pos)
                self.game[y_pos][x_pos*(y_pos+1)] = {pos: 'X'}
                print(self.game)
                # self.check_game_over()
                # self.player_turn = False

                # self.computer_choice()
        else:
            pass

    def computer_choice(self):
        self.choice = random.choice(self.choices)
        print(self.choice)
        self.draw('O', self.choice)
        self.choices.remove(self.choice)
        self.game[self.choice] = 'O'
        self.check_game_over()
        self.player_turn = True

    def draw(self, letter, pos):
        x, y = self.centers[pos][1], self.centers[pos][0]
        color = 'blue' if letter == 'O' else 'red'
        self.canvas.create_text(
            x, y, text=letter, font=('Times', 44), fill=color)

    def check_game_over(self):
        # Check rows

        for i in [0, 3, 6]:
            if self.game[i].count(self.game[i][0]) == len(self.game[i]) and self.game[i] != None:
                # if self.game[i] == self.game[i+1] == self.game[i+2] and self.game[i] != None:
                #     self.end_game(f"{self.game[i]} won")

                #     return
                return self.end_game(f"{self.game[i]} won")

        for i in [0, 1, 2]:
            if self.game[i] == self.game[i+3] == self.game[i+6] and self.game[i] != None:
                self.end_game(f"{self.game[i]} won")

                return

        if self.game[0] == self.game[4] == self.game[8] and self.game[0] != None:
            self.end_game(f"{self.game[0]} won")
            return

        if self.game[2] == self.game[4] == self.game[6] and self.game[2] != None:
            self.end_game(f"{self.game[2]} won")
            return

    def end_game(self, message):
        messagebox.showinfo(title='Game Over', message=message)
        self.root.destroy()

    def get_pos(self, x, y):
        """returns board position based on x and y coords"""
        x_pos, y_pos = 0, 0
        for edge in self.edges:
            x_pos = x_pos+1 if x > edge else x_pos
            y_pos = y_pos+1 if y > edge else y_pos

        pos = y_pos*self.size + x_pos
        return pos, x_pos, y_pos


ttc = TicTacToe(5, 100)
