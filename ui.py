from tkinter import *
from test import *
import os

class mainwindow():
    def __init__(self, root):

        self.root = root

        mainframe = Frame(root)
        mainframe.grid(row = 0, column = 1)

        sideframe = Frame(root)
        sideframe.grid(row = 0, column = 0)

        entryframe = Frame(sideframe)
        entryframe.grid(row = 0, column = 0)

        Label(entryframe, text = "placeholder").grid(row = 0, column = 0)

        buttonframe = Frame(sideframe)
        buttonframe.grid(row = 1, column = 0)

        Button(buttonframe, width = 10, text = "draw", command = self.draw).grid(row = 0, column = 0)
        Button(buttonframe, width = 10, text = "clear", command = self.clear).grid(row = 0, column = 1)
        Button(buttonframe, width = 10, text = "make piece", command = self.make).grid(row = 1, column = 0)

        self.canvas = Canvas(mainframe, width = 1000, height = 1000, bg = "white")
        self.canvas.grid(row = 0, column = 0)

    def clear(self):
        self.canvas.create_rectangle(0, 0, 1000, 1000, outline = "white", fill = "white")

    def make(self):
        make_piece_window(self.root)

    def draw(self):
        self.clear()
        n = 1000
        grid = outcome_2_knights(n)
        color = "white"
        for i in range(n):
            for j in range(n):
                flag = grid[i][j]
                if flag == 0:
                    color = "white"
                elif flag == 1:
                    color = "blue"
                elif flag == 2:
                    color = "red"
                elif flag == 3:
                    color = "blue"
                elif flag == 4:
                    color = "green"
                elif flag == 5:
                    color = "yellow"
                elif flag == 6:
                    color = "purple"
                self.canvas.create_rectangle(j, i, j + 1, i + 1, outline = color)

class make_piece_window():
    def __init__(self, root):

        window = Toplevel(root)
        self.window = window

        mainframe = Frame(self.window)
        mainframe.grid(row = 1, column = 0)

        self.targets = [[BooleanVar(value = False) for _ in range(9)] for _ in range(9)]
        self.checks = [["" for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.checks[i][j] = Checkbutton(mainframe, variable = self.targets[i][j])
                self.checks[i][j].grid(row = i, column = j)

        self.checks[4][4].config(state = DISABLED)
        self.checks[4][4].config(bg = "green")

        topframe = Frame(self.window)
        topframe.grid(row = 0, column = 0)

        self.file_name = StringVar()
        Label(topframe, text = "Enter file name:").grid(row = 0, column = 0)
        Entry(topframe, textvariable = self.file_name).grid(row = 1, column = 0)

        bottomframe = Frame(self.window)
        bottomframe.grid(row = 2, column = 0)

        Button(bottomframe, text = "Save", command = self.save_piece).grid(row = 0, column = 0)
        window.bind("<Return>", self.save_piece)

    def save_piece(self, *args):
        data = ""
        for i in range(9):
            for j in range(9):
                if self.targets[i][j].get():
                    data += f"{4 - i},{4 - j}\n"
        self.data = data[:-1]
        
        save_path = "./pieces"

        if not os.path.exists(save_path):
            os.mkdir(save_path)

        self.new_file = self.file_name.get() + ".txt"
        if self.new_file in os.listdir(save_path):
            overwrite_window(self.data, self.new_file, self.window, save_path)
        else:
            with open(os.path.join(save_path, self.new_file), 'w') as f:
                f.write(data)
            self.window.destroy()

class overwrite_window:
    def __init__(self, data, file_name, prev_window, save_path):
        self.data = data
        self.file_name = file_name
        self.save_path = save_path

        self.window = Toplevel(prev_window)
        self.prev_window = prev_window

        topframe = Frame(self.window)
        topframe.grid(row = 0, column = 0)

        Label(topframe, text = "File already exists. Overwrite?").grid(column = 0, row = 0)

        bottomframe = Frame(self.window)
        bottomframe.grid(row = 1, column = 0)

        Button(bottomframe, width = 3, text = "Yes", command = self.replace_file).grid(column = 0, row = 0)
        Button(bottomframe, width = 3, text = "No", command = self.dont).grid(column = 1, row =0)

    def replace_file(self):
        with open(os.path.join(self.save_path, self.file_name), 'w') as f:
            f.write(self.data)
        self.window.destroy()
        self.prev_window.destroy()

    def dont(self):
        self.window.destroy()