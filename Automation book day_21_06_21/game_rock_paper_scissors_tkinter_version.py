#This is the try to present the game rock,paper,scissors in GUI.
import tkinter
import tkinter.messagebox
import random

class Game:
    def __init__(self):

        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.wins = 0
        self.losses = 0
        self.ties = 0

        while True:
            tkinter.messagebox.showinfo('wins,losses,ties','wins=' + str(self.wins) + '\nlosses=' + str(self.losses) +
                                        '\nties=' + str(self.ties))

            self.radio_var = tkinter.IntVar()

            self.rb1 = tkinter.Radiobutton(self.top_frame, text='rock',variable=self.radio_var,value=1)
            self.rb2 = tkinter.Radiobutton(self.top_frame, text='paper',variable=self.radio_var,value=2)
            self.rb3 = tkinter.Radiobutton(self.top_frame,text='scissors', variable=self.radio_var,value=3)

            self.rb1.pack()
            self.rb2.pack()
            self.rb3.pack()

            self.ok_button = tkinter.Button(self.bottom_frame,text='ok',command=self.start_game)
            self.quit_button = tkinter.Button(self.bottom_frame,text='quit',command=self.window.destroy)
            self.ok_button.pack(side='left')
            self.quit_button.pack(side='left')

            tkinter.mainloop()
    def start_game(self):


        #plyer choice

        while True:
            if self.radio_var.get() == 1:
                self.plyer_choice = 'r'
            elif self.radio_var.get() == 2:
                self.plyer_choice = 'p'
            elif self.radio_var.get() == 3:
                self.plyer_choice = 's'

            #computer choice
            self.comp_number = random.randint(1, 3)
            if self.comp_number == 1:
                self.comp_move = 'r'
            elif self.comp_number == 2:
                self.comp_move = 'p'
            elif self.comp_number == 3:
                self.comp_move = 's'

            #display and record the win/loose/tie
            if self.plyer_choice == self.comp_move:
                self.ties += 1
                tkinter.messagebox.showinfo('it is a tie','it is a tie')
                #wins on the plyer side
            elif self.plyer_choice == 'r' and self.comp_move == 's':
                self.wins += 1
                tkinter.messagebox.showinfo('plyer wins','plyer wins')
            elif self.plyer_choice == 'p' and self.comp_move == 'r':
                self.wins += 1
                tkinter.messagebox.showinfo('plyer wins','plyer wins')
            elif self.plyer_choice == 's' and self.comp_move == 'p':
                self.wins += 1
                tkinter.messagebox.showinfo('plyer wins', 'plyer wins')
            #losses on the plyer side
            elif self.plyer_choice == 'r' and self.comp_move == 'p':
                self.losses += 1
                tkinter.messagebox.showinfo('plyer losses', 'plyer losses')
            elif self.plyer_choice == 'p' and self.comp_move == 's':
                self.losses += 1
                tkinter.messagebox.showinfo('plyer losses', 'plyer losses')
            elif self.plyer_choice == 's' and self.comp_move == 'r':
                self.losses += 1
                tkinter.messagebox.showinfo(('plyer losses','plyer losses'))

            tkinter.messagebox.showinfo('ties, wins, looses','ties=' + str(self.ties) + '\nwins=' + str(self.wins) +

                                        '\nlosses=' + str(self.losses))
            break

my_game = Game()
























