from tkinter import *
import random
import os
from tkinter.messagebox import showinfo


class c:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Game:

    def __init__(self):

        self.window = Tk()

        self.window.bind("<Key>", self.CommandButton1)

        # importants variables (usefull ones)
        self.tries = []
        self.words_limit = 5
        self.cbg = "#404040"
        self.fc = "#DADADA"
        self.font = "DejaVu Sans Condensed"

        with open("mots.txt", "r+") as f:
            self.words = f.readlines()

        self.guess = ""
        while len(self.guess) != self.words_limit:
            self.guess = random.choice(self.words)
            self.guess = self.guess.strip("\n")
        print(self.guess)

        # 0 = Nothing, 1 = NotHere, 2 = Yes, 3 = Exactly
        self.alphabet = [[abc, 0] for abc in "abcdefghijklmnopqrstuvwxyz"]
        # print(self.alphabet)

        self.window.title("Wordle")
        self.window.geometry("1000x800")
        self.window.minsize(1000, 800)
        self.window.maxsize(1000, 800)
        self.window.iconbitmap("icone.ico")
        self.window.config(background=self.cbg, cursor="plus")

        # definition of mains frames
        self.display_word = Frame(self.window, bg=self.cbg)
        self.display_word_2 = Frame(self.window, bg=self.cbg)
        self.display_word_3 = Frame(self.window, bg=self.cbg)
        self.display_word_4 = Frame(self.window, bg=self.cbg)
        self.display_word_5 = Frame(self.window, bg=self.cbg)
        self.display_word_6 = Frame(self.window, bg=self.cbg)

        # definition of informatives Frames
        self.geoguessr = Frame(self.window, bg=self.cbg)
        self.infos_frame = Frame(self.geoguessr, bg=self.cbg)
        self.abc = Frame(self.geoguessr, bg=self.cbg)

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.geoguessr.pack(expand=NO, side=BOTTOM)
        self.infos_frame.pack(expand=NO, side=BOTTOM)
        self.abc.pack(expand=NO, side=BOTTOM)

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_menu_bar()
        self.create_abc(self.alphabet)

    def create_menu_bar(self):
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.window.config(menu=menubar)

    def donothing(self):
        x = 0

    def create_labels(self):
        title_lbl = Label(self.window, text="Wordle   ".upper(), bg=self.cbg, font=(
            self.font, 45
        ), fg=self.fc)
        title_lbl.pack(side=TOP, pady=5, padx=5)

        self.infos = Label(self.infos_frame, text="hello".upper(), bg=self.cbg, font=(
            self.font, 20
        ), fg=self.fc)
        self.infos.pack(side=TOP, pady=5, padx=5, fill=BOTH)

    def create_abc(self, alphabet):
        for widgets in self.abc.winfo_children():
            widgets.destroy()

        for els in alphabet:
            if els[1] == 1:
                show_l = Label(self.abc, text=els[0], bg="#404040",
                               font=(self.font, 15),
                               fg="red")
            elif els[1] == 2:
                show_l = Label(self.abc, text=els[0], bg="#404040",
                               font=(self.font, 15),
                               fg="yellow")
            elif els[1] == 3:
                show_l = Label(self.abc, text=els[0], bg="#404040",
                               font=(self.font, 15),
                               fg="green")
            else:
                show_l = Label(self.abc, text=els[0], bg="#404040",
                               font=(self.font, 15),
                               fg="white")
            show_l.pack(side=LEFT)

    def create_entries(self):
        global player_entry
        player_entry = Entry(self.geoguessr, bg="white")
        player_entry.pack(fill=X, side=BOTTOM, pady=10)

    def CommandButton1(self, event):

        if event.keysym == "Return":
            pass
        else:
            return

        word = player_entry.get().lower()

        if word == self.guess.lower():
            return print("WON")

        if word + "\n" not in self.words:
            self.infos["text"] = "mot \ninnexistant"
            player_entry.delete(0, 100)
            return

        if len(word) != self.words_limit:
            self.infos["text"] = f"mots de {self.words_limit} lettres\nseulement"
        elif word in self.tries:
            player_entry.delete(0, 100)
            self.infos["text"] = f"'{word}' \ndéjà utilisé"
        else:
            player_entry.delete(0, 100)
            self.tries.append(word)
            index = self.tries.index(word)
            # word = "".join([l for l in word]).upper()
            if index == 0:
                self.elp_v3(word, self.display_word)
                self.display_word.pack(expand=NO, side=TOP)
            elif index == 1:
                self.elp_v3(word, self.display_word_2)
                self.display_word_2.pack(expand=NO, side=TOP)
            elif index == 2:
                self.elp_v3(word, self.display_word_3)
                self.display_word_3.pack(expand=NO, side=TOP)
            elif index == 3:
                self.elp_v3(word, self.display_word_4)
                self.display_word_4.pack(expand=NO, side=TOP)
            elif index == 4:
                self.elp_v3(word, self.display_word_5)
                self.display_word_5.pack(expand=NO, side=TOP)
            elif index == 5:
                self.elp_v3(word, self.display_word_6)
                self.display_word_6.pack(expand=NO, side=TOP)

    def elp_v3(self, word, display):
        ml = self.fast_l(word)
        gl = self.fast_l(self.guess)

        for el in ml:
            is_place = False
            is_here = False
            for le in gl:
                if el[0] == le[0]:
                    if el[1] == le[1]:
                        is_place = True
                    else:
                        is_here = True
            if is_place:
                print(f"{c.GREEN}letter: {el[0]}{c.ENDC}")
                stats_label = Label(display, text=el[0], bg="#5C5C5C", font=(self.font, 40), fg="green")
                for om in self.alphabet:
                    if el[0] == om[0]:
                        om[1] = 3
            elif is_here:
                print(f"{c.CYAN}letter: {el[0]}{c.ENDC}")
                stats_label = Label(display, text=el[0], bg="#5C5C5C", font=(self.font, 40), fg="yellow")
                for om in self.alphabet:
                    if el[0] == om[0]:
                        if om[1] != 3:
                            om[1] = 2
            else:
                print(f"letter: {el[0]}")
                stats_label = Label(display, text=el[0], bg="#5C5C5C", font=(self.font, 40), fg="white")
                for om in self.alphabet:
                    if el[0] == om[0]:
                        om[1] = 1
            stats_label.pack(expand=YES, side=LEFT)
            self.create_abc(self.alphabet)
            self.infos["text"] = "nice"

    def fast_l(self, word_l):
        index = 0
        list_l = []
        for l_l in word_l:
            list_l.append((l_l, index))
            index += 1
        return list_l

    """
    def elp_v2(self, word, display):
        guess = self.guess
        mot = word
        indexes = []
        alread = False
        olread = False
        for l in mot:
            list(mot)
            list(guess)
            print("=" * 50)
            print(c.GREEN + "BASE LETTER: " + l.upper() + c.ENDC)

            # check si déja la lettre est dans le mot
            if l in guess:
                # est-ce que la lettre est plus de 2 fois dans le mot :
                print(f"La lettre est : {guess.count(l)} fois dans guess")
                print(f"La lettre est : {mot.count(l)} fois dans le mot")
                if guess.count(l) >= 2:
                    print("<!>" * 5)
                    if alread:
                        print("-" * 50)
                        n = guess.index(l, guess.index(l) + 1)
                        print("letters :", guess[n], mot[n])
                        print("indexes :", n)
                        # check
                        if guess[n] == mot[n]:
                            print("<!> les deux lettres sont au même endroit dans le mot !")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="green")
                        else:
                            print("<!> les deux lettres sont pas au même endroit")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="yellow")
                    else:
                        print("=" * 50)
                        n = guess.index(l)
                        print("letters :", guess[n], mot[n])
                        print("indexes :", n)
                        if guess[n] == mot[n]:
                            print("(2 fois dans guess) les deux lettres sont au même endroit dans le mot !")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="green")
                        else:
                            print("(2 fois dans guess) les deux lettres sont pas au même endroit")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="yellow")
                    alread = True

                elif mot.count(l) >= 2:
                    print("<!> RELOU <!>")
                    if olread:
                        print("-" * 50)
                        n = guess.index(l, mot.index(l) + 1)
                        print("letters :", guess[n], mot[n])
                        print("indexes :", n)
                        if guess[n] == mot[n]:
                            print("<!> les deux lettres sont au même endroit dans le mot !")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="green")
                        else:
                            print("<!> les deux lettres sont pas au même endroit")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="yellow")
                    else:
                        print("=" * 50)
                        n = mot.index(l)
                        print("letters :", guess[n], mot[n])
                        print("indexes :", n)
                        # check
                        indexes.append(n)
                        if guess[n] == mot[n]:
                            print("(2 fois dans mot) les deux lettres sont au même endroit dans le mot !")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="green")
                        else:
                            print("(2 fois dans mot) les deux lettres sont pas au même endroit")
                            stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="yellow")
                    olread = True

                # si non elle n'est pas plus de 2 fois donc
                else:
                    n = mot.index(l)
                    print("lettres :", guess[n], mot[n])
                    print("index :", n)
                    if guess[n] == mot[n]:
                        print("les deux lettres sont au même endroit dans le mot !")
                        stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="green")
                    else:
                        print("la lettre est dans le mot mais pas au bon endroit")
                        stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="yellow")
            else:
                print(l, "MAUVAIS LETTRE !")
                stats_label = Label(display, text=l, bg="#5C5C5C", font=("Roboto", 40), fg="white")
            stats_label.pack(expand=YES, side=LEFT)
            self.infos"text"] = "Kind remember: I love you !"
        print(self.tries)
        """


app = Game()
app.window.mainloop()
