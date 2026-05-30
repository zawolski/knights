from tkinter import *
from tkinter import ttk
from test import *
import os


class mainwindow():
    def __init__(self, root):

        self.root = root

        self.open_window = []

        mainframe = Frame(root)
        mainframe.grid(row = 0, column = 1)

        sideframe = Frame(root)
        sideframe.grid(row = 0, column = 0)

        Frame(sideframe, width = 100, height = 200).grid(row = 1, column = 0)

        entryframe = Frame(sideframe)
        entryframe.grid(row = 0, column = 0, sticky = "N")

        Label(entryframe, text = "Pieces:").grid(row = 0, column = 0)
        Label(entryframe, text = "Colors:").grid(row = 0, column = 1)

        self.piece_boxes = ["" for _ in range(6)]
        self.piece_vars = [StringVar() for _ in range(6)]

        for i in range(6):
            self.piece_boxes[i] = ttk.Combobox(entryframe, width = 15, textvariable = self.piece_vars[i])
            self.piece_boxes[i].grid(row = i + 1, column = 0, pady = 10, padx = 5)
            self.piece_boxes[i].state(["readonly"])
        self.set_piece_options()

        self.color_boxes = ["" for _ in range(7)]
        self.color_vars = [StringVar() for _ in range(7)]

        c_list = self.color_list()

        for i in range(7):
            self.color_boxes[i] = ttk.Combobox(entryframe, width = 15, textvariable = self.color_vars[i])
            self.color_boxes[i].grid(row = i + 1, column = 1, pady = 10)
            #self.color_boxes[i].state(["readonly"])
            self.color_boxes[i]["values"] = tuple(c_list)
            self.color_vars[i].set(c_list[i])
            self.color_boxes[i].set(c_list[i])

        Label(entryframe, width = 15, text = "Background: ").grid(row = 7, column = 0)

        buttonframe = Frame(sideframe)
        buttonframe.grid(row = 2, column = 0, sticky = "S")

        Button(buttonframe, width = 15, text = "draw", command = self.draw2).grid(row = 0, column = 0, padx = 5, pady = 10)
        Button(buttonframe, width = 15, text = "clear", command = self.clear).grid(row = 0, column = 1)
        Button(buttonframe, width = 15, text = "make piece", command = self.make).grid(row = 1, column = 0)
        Button(buttonframe, width = 15, text = "view piece", command = self.check).grid(row = 1, column = 1)

        self.canvas = Canvas(mainframe, width = 1000, height = 1000, bg = "white")
        self.canvas.grid(row = 0, column = 0)

    def clear(self):
        self.canvas.create_rectangle(0, 0, 1000, 1000, outline = "white", fill = "white")

    def make(self):
        for window in self.open_window:
            window.destroy()
        make_piece_window(self.root, self.open_window, self)

    def check(self):
        for window in self.open_window:
            window.destroy()
        view_piece_window(self.root, self.open_window)

    def set_piece_options(self):
        files = []
        for file in os.listdir("./pieces"):
            files.append(file[:-4])
        
        files.sort()
        none_list = ["none"]
        none_list.extend(files)

        for i in range(2):
            self.piece_boxes[i]["values"] = tuple(files)
            self.piece_vars[i].set(files[0])
            self.piece_boxes[i].set(files[0])

        for i in range(2, 6):
            self.piece_boxes[i]["values"] = tuple(none_list)
            self.piece_vars[i].set(none_list[0])
            self.piece_boxes[i].set(none_list[0])

    def color_list(self):
        c_list = [
            "red",
            "green",
            "blue",
            "yellow",
            "purple",
            "orange",
            "white",
            "black"
        ]
        return c_list

    # def draw(self):
    #     self.clear()
    #     n = 1000
    #     # grid = outcome_2_knights(n)
    #     grid = outcome_3_knights(n)
    #     # grid = outcome_elephant_camel(n)
    #     color = "white"
    #     for i in range(n):
    #         for j in range(n):
    #             flag = grid[i][j]
    #             if flag == 0:
    #                 color = "white"
    #             elif flag == 1:
    #                 color = "black"
    #             elif flag == 2:
    #                 color = "yellow"
    #             elif flag == 3:
    #                 color = "blue"
    #             elif flag == 4:
    #                 color = "green"
    #             elif flag == 5:
    #                 color = "yellow"
    #             elif flag == 6:
    #                 color = "purple"
    #             self.canvas.create_rectangle(j, i, j + 1, i + 1, outline = color)

    def single_color_check(self, c_string):
        widget = self.root
        try:
            widget.winfo_rgb(c_string)
            return True
        except:
            return False

    def full_color_check(self):
        bad_colors = []
        for i in range(7):
            if not self.single_color_check(self.color_boxes[i].get()):
                bad_colors.append(i)
        return bad_colors


    def draw2(self):
        for window in self.open_window:
            window.destroy()
        self.clear()
        bad_colors = self.full_color_check()
        if len(bad_colors) == 0:
            n = 1000
            plist = []
            for box in self.piece_boxes:
                if box.get() != "none":
                    file_name = box.get() + ".txt"
                    move_list = load(file_name)
                    plist.append(piece(box.get(), move_list))
            grid = outcome(n, plist)
            color = self.color_boxes[6].get()
            for i in range(n):
                for j in range(n):
                    flag = grid[i][j]
                    if flag == 0:
                        color = self.color_boxes[6].get()
                    elif flag == 1:
                        color = self.color_boxes[0].get()
                    elif flag == 2:
                        color = self.color_boxes[1].get()
                    elif flag == 3:
                        color = self.color_boxes[2].get()
                    elif flag == 4:
                        color = self.color_boxes[3].get()
                    elif flag == 5:
                        color = self.color_boxes[4].get()
                    elif flag == 6:
                        color = self.color_boxes[5].get()
                    self.canvas.create_rectangle(j, i, j + 1, i + 1, outline = color)
        else:
            bad_color_window(self.root, self.open_window, bad_colors)

class bad_color_window:
    def __init__(self, root, open_window, bad_colors):
        window = Toplevel(root)
        open_window.append(window)
        self.window = window

        mainframe = Frame(window)
        mainframe.grid(row = 0, column = 0)

        Label(mainframe, text = "The following pieces have invalid colors:").grid(row = 0, column = 0)
        
        for i in range(6):
            if i in bad_colors:
                Label(mainframe, text = f"Piece {i + 1}").grid(row = i + 1, column = 0)

        if 6 in bad_colors:
            Label(mainframe, text = "Background").grid(row = 7, column = 0)

        Button(mainframe, text = "Okay", command = self.close_window).grid(row = 8, column = 0)

    def close_window(self):
        self.window.destroy()

class view_piece_window():
    def __init__(self, root, open_window):
        window = Toplevel(root)

        open_window.append(window)

        mainframe = Frame(window)
        mainframe.grid(row = 1, column = 0)

        self.canvas = Canvas(mainframe, width = 450, height = 450, bg = "white")
        self.canvas.grid(row = 0, column = 0)
        self.reset_board()

        topframe = Frame(window)
        topframe.grid(row = 0, column = 0)

        files = []
        for file in os.listdir("./pieces"):
            files.append(file[:-4])

        files.sort()

        self.target = StringVar(value = files[0])
        Label(topframe, text = "Select a piece to view:").grid(row = 0, column = 0)
        self.selection_box = ttk.Combobox(topframe, width = 20, textvariable = self.target)
        self.selection_box["values"] = tuple(files)
        self.selection_box.grid(row = 1, column = 0)
        self.selection_box.set(files[0])
        self.selection_box.state(["readonly"])

        bottomframe = Frame(window)
        bottomframe.grid(row = 2, column = 0)

        Button(bottomframe, text = "View", command = self.show).grid(row = 0, column = 0)

    def show(self):
        self.reset_board()
        file_name = self.selection_box.get() + ".txt"
        move_list = load(file_name)
        for move in move_list:
            y = (4 - move[0]) * 50
            x = (4 - move[1]) * 50
            self.canvas.create_rectangle(x, y, x + 50, y + 50, outline = "red", fill = "red")

    def reset_board(self):
        self.canvas.create_rectangle(0, 0, 450, 450, outline = "white", fill = "white")
        for i in range(4):
            for j in range(5):
                x = ((2 * i) + 1) * 50
                y = 2 * j * 50
                self.canvas.create_rectangle(x, y, x + 50, y + 50, outline = "black", fill = "black")
        for i in range(5):
            for j in range(4):
                x = 2 * i * 50
                y = ((2 * j) + 1) * 50
                self.canvas.create_rectangle(x, y, x + 50, y + 50, outline = "black", fill = "black")
        self.canvas.create_rectangle(200, 200, 250, 250, outline = "green", fill = "green")


class make_piece_window():
    def __init__(self, root, open_window, prev):
        self.prev = prev

        window = Toplevel(root)
        self.window = window

        open_window.append(window)

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
                f.write(self.data)
            self.prev.set_piece_options()
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