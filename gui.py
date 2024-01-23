from tkinter import *


class App(Tk):
    """
    This class is used to define the main window by using tkinter graphic interface module
    """

    def __init__(self):
        super().__init__()
        self.configure(bg='#8e8e8e')
        self.title("VisioVault")
        self.resizable(False, False)

