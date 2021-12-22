# coding UTF-8
from tkinter import *
import tkinter

class Player:

    def __init__(self, player_id):
        self.status = 0
        self.player_id = player_id
        print('player %d'% self.player_id)


class Round:
    
    def __init__(self):
        self.round = 0
        self.current_player = 1
        # player 1 joue
        # on vérifie si il y a un gagnant ou si le nombre de tour <=5
        # player 2 joue
        # on vérifie si il y a un gagnant ou si nbre tour <=4
        print('%d round'% self.round)
    
    @property
    def get_current_player(self):
        return self.current_player

    def set_current_player(self, player):
        if player == 1:
            self.current_player = 2
        else:
            self.current_player = 1



class Grid:

    SIZE = 3

    def __init__(self):
        self.grid = [self.__cell for cell in self.__raw]
        print('new grid :',self.grid)

    @property
    def __raw(self):
        return [raw for raw in range(self.SIZE)]

    @property
    def __cell(self):
        return [0 for cell in range(self.SIZE)]

    def get_length(self):
        return len(self.grid)


class Board:

    def __init__(self):
        self.board = {
            'grid': Grid(),
            'player1': Player(1),
            'player2': Player(2),
            'round': Round(),
            'window': Tk()
        }

        self.APPLE = tkinter.PhotoImage(file="img/apple.png") # player1
        self.GRAPPES = tkinter.PhotoImage(file="img/grappes.png") # player2
        self.BLANK = tkinter.PhotoImage(file="img/blank.png")

        self.message = self.set_message()
        self.GUI_gameboard()

        print('new board created!')

    def window(self):
        return self.board['window']

    def get_grid(self):
        return self.board['grid'].get_length()

    def set_message(self, player=None):
        if player == 1 :
            return 'GO apple!'
        elif player == 2:
            return 'GO grappes!'
        else:
            return "Let's GOoo!"
    
    def get_message(self):
            return self.message

    def on_click(self, btn):
        player = self.board['round'].get_current_player
        if (player == 1 and btn.cget('image') == 'pyimage3'):
            btn.configure(image=self.APPLE)
        elif (player == 2 and btn.cget('image') == 'pyimage3'):
            btn.configure(image=self.GRAPPES)
        self.board['round'].set_current_player(player)
        self.set_message(player)
        
    def get_message_label(self, gameboard):
        return tkinter.Label(gameboard, text=self.get_message(), bg="#5cc7b2", font=14, pady=10).pack(side='top', fill="x")

    def GUI_gameboard(self):

        gameboard = self.window()

        # Creating app window
        gameboard.title("audreyntep")
        gameboard.iconbitmap("img/antep.ico")
        gameboard.configure(background="white")

        # Window dimensions
        window_dimension = 500
        gameboard.geometry("{side}x{side}+{margin_left}+100".format(side=window_dimension, margin_left=int(gameboard.winfo_screenwidth() / 2 - window_dimension / 2)))
        gameboard.resizable(width=False, height=False)
        
        # Window content
        tkinter.Label(gameboard, text="Tic Tac Toe", font=("Courrier", 18, "bold"), pady=20).pack(side='top', fill="x")

        self.get_message_label(gameboard)
        
        frame = tkinter.Frame(gameboard, bg="yellow", height=window_dimension-20)

        # Creating cards
        raw1 = tkinter.Frame(frame, bg="teal")
        index=0
        for cell in range(3):
            card = tkinter.Button(raw1, bg="white", image=self.BLANK, width=100, height=100,padx=10, pady=10)
            card.configure(command=lambda btn=card: self.on_click(btn))
            card.grid(row=0, column=index)
            index += 1
        raw1.pack(expand=YES)

        raw2 = tkinter.Frame(frame, bg="teal")
        index=0
        for cell in range(3):
            card = tkinter.Button(raw2, bg="white", image=self.BLANK, width=100, height=100,padx=10, pady=10)
            card.configure(command=lambda btn=card: self.on_click(btn))
            card.grid(row=0, column=index)
            index += 1
        raw2.pack(expand=YES)

        raw3 = tkinter.Frame(frame, bg="teal")
        index=0
        for cell in range(3):
            card = tkinter.Button(raw3, bg="white", image=self.BLANK, width=100, height=100,padx=10, pady=10)
            card.configure(command=lambda btn=card: self.on_click(btn))
            card.grid(row=0, column=index)
            index += 1
        raw3.pack(expand=YES)
        
        frame.pack(expand=YES, pady=10)


