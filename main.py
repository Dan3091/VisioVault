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

app = App(add_app, reset, start, face_id_security, select_app)