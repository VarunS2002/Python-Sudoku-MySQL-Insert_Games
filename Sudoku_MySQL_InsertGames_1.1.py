from tkinter import *
from tkinter import messagebox
import os
import webbrowser
import mysql.connector as sql


class Box:

    def __init__(self, root):

        # Main Window

        self.root = root
        root.title("Insert Games")
        root.resizable(False, False)

        # Default Connection Properties

        self.host = "localhost"
        self.username = "root"
        self.password = ""

        # Manual Connection Properties

        config_exists = os.path.isfile("mysql_config.txt")
        if config_exists:
            config = open("mysql_config.txt", "r")
            read_save = config.read()
            list_items = read_save.split("\n")
            if len(list_items[3]) != 0:
                self.host = list_items[3]
            if len(list_items[5]) != 0:
                self.username = list_items[5]
            if len(list_items[7]) != 0:
                self.password = list_items[7]
        else:
            pass

        # Database Connection

        try:
            self.my_db = sql.connect(
                host=f"{self.host}",
                user=f"{self.username}",
                passwd=f"{self.password}"
            )

        # Connection Error Window

        except:
            self.root.title("Error")
            self.root.geometry("200x30")
            error_message = Label(self.root, text="Incorrect credentials for MySQL")
            error_message.pack(fill="y", expand="1")
            self.root.mainloop()
            quit()

        # Setting Database and Cursor

        self.c = self.my_db.cursor()
        self.c.execute("use sudoku")

        # EntryBox and Game Lists

        self.boxes = []
        self.game = []

    # Quit Function

    def close(self):
        ask_quit = messagebox.askyesno("Quit", "Do you want to quit?")
        if ask_quit:
            quit()
        elif not ask_quit:
            pass

    # Releases

    def releases(self):
        webbrowser.open_new("https://github.com/VarunS2002/Python-Sudoku-MySQL-Insert_Games/releases/")
        self.info.attributes('-topmost', False)

    # Sources

    def sources(self):
        webbrowser.open_new("https://github.com/VarunS2002/Python-Sudoku-MySQL-Insert_Games/")
        self.info.attributes('-topmost', False)

    # About Window

    def about_window(self):
        self.info = Toplevel()
        self.info.title("About")
        self.info.resizable(False, False)
        self.info.geometry('220x100')
        self.info.attributes('-topmost', True)
        self.info.grab_set()
        self.info.focus_force()
        return self.info

    # About Function

    def about(self):
        self.info = self.about_window()

        version = Label(self.info, text="Version: 1.1")
        version.pack(side='top', pady="5")
        release = Button(self.info, text="Releases", fg="blue", cursor="hand2", borderwidth=0, command=self.releases)
        release.pack(side='top', pady="5")
        source = Button(self.info, text="Sources", fg="blue", cursor="hand2", borderwidth=0, command=self.sources)
        source.pack(side='top', pady="5")

        self.info.mainloop()

    # Insert into Start Function

    def insert_start(self):
        self.c.execute("select max(gno) from solved")
        self.next_gno = self.c.fetchall()[0][0] + 1
        self.game.append(self.next_gno)

        # Validating Values

        for x in range(81):
            try:
                self.game.append(int(self.boxes[x].get()))
            except:
                messagebox.showwarning("Incorrect Values", "Please enter correct values")
                self.game.clear()
                return
        for q in range(1, 82):
            if 10 > int(self.game[q]) >= 0:
                pass
            else:
                messagebox.showwarning("Incorrect Values", "Please enter correct values")
                self.game.clear()
                return

        self.c.execute(f"insert into start values{tuple(self.game)}")

        # Setting Option Menu Attributes

        self.options.entryconfig(self.options.index("Insert into start"), state=DISABLED)
        self.options.entryconfig(self.options.index("Insert into solved"), state=NORMAL)

        messagebox.showinfo("Inserted", "Values have been inserted into start")

    # Insert into Solved Function

    def insert_solved(self):
        self.game.clear()
        self.game.append(self.next_gno)

        # Validating Values

        for x in range(81):
            try:
                self.game.append(int(self.boxes[x].get()))
            except:
                messagebox.showwarning("Incorrect Values", "Please enter correct values")
                self.game.clear()
                return
        for q in range(1, 82):
            if 10 > int(self.game[q]) >= 1:
                pass
            else:
                messagebox.showwarning("Incorrect Values", "Please enter correct values")
                self.game.clear()
                return

        self.c.execute(f"insert into solved values{tuple(self.game)}")

        # Setting Option Menu Attributes

        self.options.entryconfig(self.options.index("Insert into solved"), state=DISABLED)
        self.options.entryconfig(self.options.index("Commit"), state=NORMAL)

        messagebox.showinfo("Inserted", "Values have been inserted into solved")

        # Setting EntryBox Attributes

        for x in range(81):
            self.boxes[x].config(state=DISABLED)

    # Commit Function

    def commit(self):
        self.my_db.commit()
        self.game.clear()

        # Setting Option Menu Attributes

        self.options.entryconfig(self.options.index("Insert into start"), state=NORMAL)
        self.options.entryconfig(self.options.index("Commit"), state=DISABLED)

        messagebox.showinfo("Committed", "Inserted values have been committed")

        # Setting EntryBox Attributes

        for x in range(81):
            self.boxes[x].config(state=NORMAL)

    # Grid Function

    def grid(self):
        i = 0
        for rowindex in range(9):

            for colindex in range(9):

                # Setting Grid Color

                if rowindex in (0, 1, 2, 6, 7, 8) and colindex in (3, 4, 5):
                    self.bg_colour = "light grey"
                elif rowindex in (3, 4, 5) and colindex in (0, 1, 2, 6, 7, 8):
                    self.bg_colour = "light grey"
                else:
                    self.bg_colour = "white"

                # Adding EntryBox Objects to List

                self.boxes.append(i)

                # Creating EntryBoxes

                self.boxes[i] = Entry(self.root, width=6, bg=self.bg_colour, relief=RAISED, justify=CENTER)
                self.boxes[i].insert(0, 0)
                self.boxes[i].grid(row=rowindex, column=colindex, sticky=N + S + E + W, ipadx=5, ipady=15)

                # Increasing Value of i for Iteration

                i += 1

    # Option Menu Function

    def create_menu(self):
        menubar = Menu(self.root)
        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label="Insert into start", command=self.insert_start)
        self.options.add_command(label="Insert into solved", command=self.insert_solved, state=DISABLED)
        self.options.add_command(label="Commit", command=self.commit, state=DISABLED)
        self.options.add_separator()
        self.options.add_command(label="About", command=self.about)
        self.options.add_command(label="Quit", command=self.close)
        menubar.add_cascade(label="Menu", menu=self.options)

        # Setting Main Window Attributes

        self.root.config(menu=menubar)
        self.root.protocol('WM_DELETE_WINDOW', self.close)


if __name__ == "__main__":
    master = Tk()
    box_instance = Box(master)
    box_instance.grid()
    box_instance.create_menu()
    master.mainloop()
