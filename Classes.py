# coding UTF-8
from tkinter import *
from tkinter import ttk
import tkinter

class Player:

    def __init__(self, id):
        self.player = {
            'id': id,
            'symbol':'',
            'GUI_symbol':'',
            'name':''
        }
        print('\n player %d created'% self.player['id'])

    @property
    def get_id(self):
        return self.player['id']

    @property
    def get_symbol(self):
        return self.player['symbol']

    @property
    def get_GUI_symbol(self):
        return self.player['GUI_symbol']

    def set_symbol(self, symbol):
        self.player['symbol'] = symbol

    def set_GUI_symbol(self, symbol):
        self.player['GUI_symbol'] = symbol

class Grid:

    def __init__(self, size):
        self.grid = self.create_grid(size)
        print('\n grid size %d x %d created' % (size,size))
        print(self.grid)

    def create_grid(self, size):
        return [[0]*size for row in range(size)]

    def print_grid(self):
        for line in self.grid:
            print(line)

    def set_cell(self, row, cell, player):
        self.grid[row][cell] = player

    def is_player_symbols_aligned(self):

        symbols_aligned = False

        # horizontal
        for line in self.grid:
            line_of_3 = any(line.count(element) == 3 for element in line if element != 0)
            if line_of_3:
                symbols_aligned = line_of_3
        
        # vertical
        columns = [[0]*3 for row in range(3)]
        for index in range(3):
            columns[0][index] = self.grid[index][0]
            columns[1][index] = self.grid[index][1]
            columns[2][index] = self.grid[index][2]
        for column in columns:
            column_of_3 = any(column.count(element) == 3 for element in column if element != 0)
            if column_of_3:
                symbols_aligned = column_of_3

        # diagonal left to right
        diagonal_l_r = []
        for cell in range(3):
            diagonal_l_r.append(self.grid[cell][cell])
        diagonal_of_3_l_r = any(diagonal_l_r.count(element) == 3 for element in diagonal_l_r if element != 0)
        if diagonal_of_3_l_r:
            symbols_aligned = diagonal_of_3_l_r

        # diagonal right to left
        diagonal_r_l = []
        diagonal_r_l.append(self.grid[0][2])
        diagonal_r_l.append(self.grid[1][1])
        diagonal_r_l.append(self.grid[2][0])
        diagonal_of_3_r_l = any(diagonal_r_l.count(element) == 3 for element in diagonal_r_l if element != 0)
        if diagonal_of_3_r_l:
            symbols_aligned = diagonal_of_3_r_l

        return symbols_aligned

    def is_grid_filled(self):
        played = 0
        for line in self.grid:
            played += line.count(1)
            played += line.count(2)
        if played == 9:
            return True
            

class Game:
    
    def __init__(self):
        self.game = {
            'players': 2,
            'grid_size': 3,
            'symbols': ['x', 'o'],
            'current_player_id': 1,
            'winner': 0
        }
        self.board = self.create_gameboard()
        print('\n game ready to start!')

    @property
    def get_players(self):
        return self.game['players']
    
    @property
    def get_grid_size(self):
        return self.game['grid_size']

    @property
    def get_symbols(self):
        return self.game['symbols']

    @property
    def get_current_player_id(self):
        return self.game['current_player_id']
    
    @property
    def get_winner(self):
        return self.game['winner']

    def get_board(self):
        return self.board

    def __set_current_player_id(self, id):
        self.game['current_player_id'] = id

    def __set_winner(self, player):
        self.game['winner'] = player

    def switch_current_player_id(self):
        if self.get_current_player_id == 1:
            self.__set_current_player_id(2)
        else:
            self.__set_current_player_id(1)

    def is_game_ended(self, cell_played, player_id):
        self.board.get_grid().set_cell(cell_played['row'], cell_played['column'], player_id)
        if self.board.get_grid().is_player_symbols_aligned():
            self.__set_winner(self.get_current_player_id)
            return True
        if self.board.get_grid().is_grid_filled():
            return True
    
    def create_gameboard(self):
        return Gameboard(grid= self.get_grid_size, players=self.get_players, symbols=self.get_symbols)

class Gameboard:

    def __init__(self, grid, players, symbols):
        self.board = {
            'grid': Grid(grid),
            'players': [],
        }
        # creating the players
        self.create_players(players)
        # assigning symbols to players
        self.assign_symbols_to_players(symbols)

        print('\n gameboard created')

    def get_grid(self):
        return self.board['grid']

    def get_player(self, player):
        return self.board['players'][player]

    def get_players(self):
        return self.board['players']

    def set_players(self, player):
        self.board['players'].append(player)

    def assign_symbols_to_players(self, symbols):
        for player in range(len(self.get_players())):
            self.get_player(player).set_symbol(symbols[player])
            print('\n player', self.get_player(player).get_id, 'plays', self.get_player(player).get_symbol)

    def create_players(self, players): 
        index = 1
        for player in range(players) :
            self.set_players(Player(index))
            index+=1

class GUI_Gameboard():

    BLANK = "img/blank.png"
    FIRST = "img/apple.png"
    SECOND = "img/grappes.png"

    def __init__(self, game):
        self.game = game
        self.board = game.get_board()
        self.create_GUI_board()

    def create_GUI_board(self):
        window = Tk()

        # Creating the app window
        window.title("audreyntep")
        window.iconbitmap("img/antep.ico")
        window.configure(background="white")

        # Fixing app window dimensions
        window_dimension = 500
        window.geometry("{side}x{side}+{margin_left}+100".format(side=window_dimension, margin_left=int(window.winfo_screenwidth() / 2 - window_dimension / 2)))
        window.resizable(width=False, height=False)

        # Filling app window content
        title = Label(window, text="Tic Tac Toe", font=("Courrier", 18, "bold"), pady=20).pack(side='top', fill="x")
        message = Label(window, text="Let' Go", bg="#5cc7b2", font=14, pady=10).pack(side='top', fill="x")

        # Creating a GUI grid with 3 rows, 3 cells each filled with blank card
        GUI_grid = Frame(window)
        blank = PhotoImage(file=self.BLANK)
        for line in range(3):
            row = Frame(GUI_grid)
            for cell in range(3):
                btn = Button(row, image=blank)
                btn.config(command=lambda btn=btn: self.on_click(btn))
                btn.grid(row=line, column=cell)
            row.grid(row=line, column=1)
        GUI_grid.pack(expand=YES)

        # assigning GUI symbols to players
        self.assign_GUI_symbols_to_players()

        return window.mainloop()

    def assign_GUI_symbols_to_players(self):
        # looping on players
        for player in self.board.get_players():
            if player.get_id == 1:
                player.set_GUI_symbol(PhotoImage(file=self.FIRST))
                print('\n player', player.get_id,'plays', self.FIRST, player.get_GUI_symbol)
            else:
                player.set_GUI_symbol(PhotoImage(file=self.SECOND))
                print('\n player', player.get_id,'plays', self.SECOND, player.get_GUI_symbol)

    def on_click(self, btn):
        # getting player with current id
        player_id = self.game.get_current_player_id
        player = self.board.get_player(player_id-1)
        # changing image
        if btn.cget('image') == 'pyimage1':
            btn.configure(image=player.get_GUI_symbol)
            # getting cell position (row and column)
            cell = btn.grid_info()
            # checking if grid is filled or if player won
            if self.game.is_game_ended(cell, player_id):
                if self.game.get_winner != 0 :
                    self.GUI_message_window("Congratulation player %d" % self.game.get_winner)
                else :
                    self.GUI_message_window('no winner!!!')
            # changing player
            else:
                self.game.switch_current_player_id()

    def GUI_message_window(self, message):
        window = Tk()
        # Creating the app window
        window.title("audreyntep")
        window.iconbitmap("img/antep.ico")
        window.configure(background="white")
        # Fixing app window dimensions
        window_dimension = 400
        window.geometry("{side}x{side}+{margin_left}+200".format(side=window_dimension, margin_left=int(window.winfo_screenwidth() / 2 - window_dimension / 2)))
        window.resizable(width=False, height=False)
        # Filling app window content
        content = Frame(window, background="white")
        message = Label(content, text=message, bg="white", font=14, padx=20, pady=20).pack()
        content.pack(expand=YES)
        return window.mainloop()



