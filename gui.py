from tkinter import *


class App(Tk):
    """
    This class is used to define the main window by using tkinter graphic interface module
    """

    def __init__(self, add_app, reset, start, face_id_security, select_app):
        self.add_app = add_app
        self.reset = reset
        self.start = start
        self.face_id_security = face_id_security
        self.select_app = select_app

        super().__init__()
        self.configure(bg='#8e8e8e')
        self.title("VisioVault")
        self.resizable(False, False)

        # Calculation of the main window position
        posx = str((self.winfo_screenwidth() // 2) - (300 // 2))
        posy = str((self.winfo_screenheight() // 2) - (500 // 2))
        self.geometry(f"300x550+{posx}+{posy}")
