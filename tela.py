import random
import string
import customtkinter
import os
import tkinter
from CTkMessagebox import CTkMessagebox
from tkinter import *

file_path = os.path.abspath('senha.png')

tela = customtkinter.CTk()
tela.geometry("300x360")
tela.title('pass-generator')
tela.configure()


img = PhotoImage(file=file_path)
img = img.subsample(9, 9)


app_img = customtkinter.CTkLabel(tela, height=60, image=img, compound='left',
                                 padx=40, anchor="nw", text="Gerador de Senha", )
app_img.place(x=2, y=0)

app_line = customtkinter.CTkLabel(
    tela, width=300, height=1, fg_color="#696969", text="")
app_line.place(x=0, y=55)

var = IntVar()
var.set(8)

app_info = customtkinter.CTkLabel(
    tela, width=300, height=25, text="Total de Caracteres para gerar nova senha:")
app_info.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


spin = Spinbox(tela, width=7, from_=0, to=20, textvariable=var)
spin.place(relx=0.25, rely=0.25, anchor=tkinter.NE)

app_password = customtkinter.CTkLabel(
    tela, width=180, height=30,  text="- - -", fg_color="#191970", text_color="#FFF")
app_password.place(relx=0.5, y=150, anchor=tkinter.CENTER)

# MAIUSCULO
opt1 = StringVar()
opt1.set(False)
app_info = customtkinter.CTkLabel(
    tela, width=300, height=25, text="ABC - Maiusculo")
app_info.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

# https://www.youtube.com/watch?v=uGI-W_HVp14
tela.mainloop()
