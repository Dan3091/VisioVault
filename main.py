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