from tkinter import *
from tkinter.messagebox import showinfo
from database_encryptor import *
from selenium import webdriver
import os
from gui import App
import time
from recognition_app import video_capture_logic, face_id


app_urls = {"Facebook": "https://www.facebook.com/",
            "Instagram": "https://www.instagram.com/"}
app_tags = {"Facebook": ["/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]",
                         "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input",
                         "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input",
                         "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button"],
            "Instagram": ["/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]",
                          "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
                          "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
                          "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]"]}

database = {}

def validate_app_name():
    """
    This function validates the select_app() function,
    if nothing is selected it returns False otherwise True
    """

    if select_app() == None:
        popup_message(f"Please, first select the app!")
        return False
    else:
        return True

def validate_email():
    """
    This function validates the email_entry, if app.email_entry.get() return an empty string,
     then it change the text from email_error label, and returns False, otherwise it returns True.
     """

    email = app.email_entry.get()
    if len(email) == 0:
        app.email_error.config(text="*Fill the Email")
        return False
    else:
        app.email_error.config(text="")
        return True

def validate_password():
    """
    This function validates the password_entry, if app.password_entry.get() return an empty string,
    then it change the text from password_error label, and returns False, otherwise it returns True.
    """

    password = app.password_entry.get()
    if len(password) == 0:
        app.password_error.config(text="*Fill the Password")
        return False
    else:
        app.password_error.config(text="")
        return True

def select_app():
    """
    app.var.get() return the selected radio button 1 or 2,
     if app.var.get() == 1 then select_app() return Facebook,
     else if app.var.get() == 2 then it returns Instagram.
     """

    if app.var.get() == "1":
        return "Facebook"
    elif app.var.get() == "2":
        return "Instagram"

def add_app():
    """
    Here the main logic of the function is to check all validations,
     if at least one validation return False, then app_name, email_name,
      and password is not saved, otherwise it will be saved in database dictionary,
      """

    global database
    x = all((validate_email(), validate_password(), validate_app_name()))
    if x:
        if select_app() not in database and select_app() not in load_data():
            database[select_app()] = [app.email_entry.get(), app.password_entry.get()]
            popup_message(f"The Credentials for {select_app()} added.")
            app.email_entry.delete(0, END)
            app.password_entry.delete(0, END)
        else:
            popup_message(f"Sorry, the Credentials for {select_app()} already exists.")
    if len(database) > 0 and select_app() != None:
        save_data()
        app.faceid_button.config(state=NORMAL)

def save_data():
    """
    Here the function call the encrypt_dict function from database_encryptor,
     to encrypt database dictionary, then it save this data like database.bin on disk.
     """

    if len(database) > 0:
        print("Enter")
        with open("database.bin", "wb+") as file:
            data = encrypt_dict(str(database))
            file.write(data)
    load_data()

def load_data():
    """
    This function will try to load the database encrypted file,
    if present it will load it and by using decrypt_dict method,
     from database_encryptor module will decrypt and return it,
      otherwise it will return an empty dictionary
      """

    try:
        with open("database.bin", "rb") as file:
            data = file.read()
            data = eval(decrypt_dict(data))
            return data
    except:
        return {}

def face_id_security():
    """
    This function is called when you click on FaceID button,
     then the face_id() function is called and assigned to response variable,
     if response return True then a popup message window will appear,
     saying that no camera was found on this computer,
      otherwise will appear a popup message saying that The face ID was saved.
      """

    response = face_id()
    if response:
        popup_message("There isn't any camera on this Computer!")
    else:
        popup_message("Face ID was saved.")
        app.reset_data_button.config(state=NORMAL)
        app.start_button.config(state=NORMAL)

def reset():
    """
    This function will delete database.bin, filekey.key and faceid.jpg from disk,
     and reset the database to an empty dictionary.
     """

    global database
    os.remove("database.bin")
    os.remove("filekey.key")
    os.remove("faceid.jpg")
    database = {}
    popup_message("All data from database was deleted.")
    app.reset_data_button.config(state=DISABLED)
    app.start_button.config(state=DISABLED)
    app.faceid_button.config(state=DISABLED)

def popup_message(message):
    """
    Here this function create a popup message window.
    """

    window = Tk()
    window.attributes('-topmost', 1)
    window.withdraw()
    return showinfo(title="Info", message=message)


def autofill(app_name):
    """
    By using selenium.webdriver module will create a webdriver object,
     then will use find_element method (using xpath type) to find the Cookies button,
      email entry, password and login button then with send method it will fill email and password entries
      after that with click method it will click on Allow cookies and LogIn buttons
      """

    url = app_urls[app_name]
    email = database[app_name][0]
    password = database[app_name][1]
    security = video_capture_logic(email)
    if security == True:
        popup_message(f"Accepted! Hi {email}, one moment and you will be redirected to your {app_name} account.")
        web_opt = webdriver.ChromeOptions()
        web_opt.add_experimental_option("detach", True)
        web = webdriver.Chrome(options=web_opt)
        web.get(url)
        log_in_button = web.find_element("xpath", app_tags[app_name][0])
        log_in_button.click()
        email_form = web.find_element("xpath", app_tags[app_name][1])
        email_form.send_keys(email)
        psw_form = web.find_element("xpath", app_tags[app_name][2])
        psw_form.send_keys(password)
        time.sleep(10)
        log_in_button1 = web.find_element("xpath", app_tags[app_name][3])
        log_in_button1.click()
    else:
        popup_message("Sorry, I can't recognize you!")

def popup_choose_app(message):
    """
    Here this function create a popup window,
     with app selection menu that are in database dictionary.
     """

    pop = Toplevel()
    pop.title("Menu")
    pop_label = Label(pop, text="Select the App:", font="Unispace 16")
    pop_label.pack(pady=10, padx=10)
    for app in database:
        pop_button = Button(pop, text=app, font="Unispace 12", command=lambda a=app:autofill(a))
        pop_button.pack(pady=5)
    bottom_padding = Label(pop)
    bottom_padding.pack()
    pop.update_idletasks()
    posx = str((pop.winfo_screenwidth() // 2) - (pop.winfo_width() // 2))
    posy = str((pop.winfo_screenheight() // 2) - (pop.winfo_height() // 2))
    pop.geometry(f"{pop.winfo_width()}x{pop.winfo_height()}+{posx}+{posy}")

def start():
    """
    The function simply call the popup_choose_app function
    """

    popup_choose_app(f"Leave the window or minimize it and go on some app website.")

def main():
    """
    The main function call the load_data function if in database there is any data the start_button,
     reset_button and faceid_button state change from DISABLED to NORMAL
     """

    global database
    database = load_data()
    if database != {} and os.path.exists('faceid.jpg'):
        app.start_button.config(state=NORMAL)
        app.reset_data_button.config(state=NORMAL)
        app.faceid_button.config(state=NORMAL)

app = App(add_app, reset, start, face_id_security, select_app)

if __name__ == "__main__":
    main()
    app.mainloop()