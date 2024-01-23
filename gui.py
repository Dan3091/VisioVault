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

        frame = Frame(self, width=280, height=530, bg="#7f7f7f")
        frame.grid(pady=10)
        frame.pack_propagate(0)
        frame.pack(pady=10)

        # Label App Name
        self.title_label = Label(frame, text="VisioVault", font="Unispace 20", bg="#7f7f7f")
        self.title_label.pack(pady=20)

        # Label Select App Name
        self.app_name_label = Label(frame, text="Select the App:", font="Unispace 14", bg="#7f7f7f")
        self.app_name_label.pack(pady=(10, 0))

        # Created 2 Radio Buttons Facebook And Instagram
        self.var = StringVar(value="not selected")
        self.facebook_bt = Radiobutton(frame, text="Facebook", variable=self.var, value=1, font="Unispace 12",
                                       command=select_app, bg="#7f7f7f")
        self.facebook_bt.pack()
        self.instagram_bt = Radiobutton(frame, text="Instagram", variable=self.var, value=2, font="Unispace 12",
                                        command=select_app, bg="#7f7f7f")
        self.instagram_bt.pack()

        # Created Email Label, Email Error Label and Email Entry
        self.email_label = Label(frame, text="Email:", font="Unispace 14", bg="#7f7f7f")
        self.email_label.pack(pady=(20, 0))
        self.email_error = Label(frame, text="", font="Unispace 10", bg="#7f7f7f", fg="#760000")
        self.email_error.pack()
        self.email_entry = Entry(frame, width=280, font="Unispace 14")
        self.email_entry.pack_propagate(0)
        self.email_entry.pack(padx=20)

        # Created Password Label, Password Error Label and Password Entry
        self.password_label = Label(frame, text="Password", font="Unispace 14", bg="#7f7f7f")
        self.password_label.pack(pady=(20, 0))
        self.password_error = Label(frame, text="", font="Unispace 10", bg="#7f7f7f", fg="#760000")
        self.password_error.pack()
        self.password_entry = Entry(frame, width=280, font="Unispace 14", show="*")
        self.password_entry.pack_propagate(0)
        self.password_entry.pack(padx=20)

        # Created 4 buttons(Add App, FaceID, Reset, Start)
        self.add_app_button = Button(frame, text="Add APP", font="Unispace 14", command=add_app, height=1, width=9)
        self.add_app_button.place(x=20, y=420)

        self.faceid_button = Button(frame, text="FaceID", font="Unispace 14", command=face_id_security, height=1,
                                    width=9, state=DISABLED)
        self.faceid_button.place(x=142, y=420)

        self.reset_data_button = Button(frame, text="Reset", font="Unispace 14", command=reset, height=1, width=9,
                                        state=DISABLED)
        self.reset_data_button.place(x=20, y=480)

        self.start_button = Button(frame, text="Start", font="Unispace 14", command=start, height=1, width=9,
                                   state=DISABLED)
        self.start_button.place(x=142, y=480)