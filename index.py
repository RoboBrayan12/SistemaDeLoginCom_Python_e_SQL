from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import dataBaser

jan = Tk()

jan.title("RW Project - Painel de Login")
jan.geometry("690x300")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="assets/icon.ico")

# Frames

LeftFrame = Frame(jan, width=200, height=300, bg="#171717", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=485, height=300, bg="#171717", relief="raise")
RightFrame.pack(side=RIGHT)

# Logo Image

logo = PhotoImage(file="assets/logo.png")

LogoLabel = Label(LeftFrame, image=logo, width=100, height=100)
LogoLabel.place(x=50, y=100)

# Login Form

UserLabel = Label(RightFrame, text="Nome de Usuário:", font=("Century Gothic", 16), bg="#171717", fg="White")
UserLabel.place(x=10, y=100)

UserEntry = ttk.Entry(RightFrame, width=40)
UserEntry.place(x=220, y=105)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 16), bg="#171717", fg="White")
PassLabel.place(x=10, y=140)

PassEntry = ttk.Entry(RightFrame, width=40, show="•")
PassEntry.place(x=220, y=145)

# Botões e Funções

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    if (not User or not Pass):
        messagebox.showwarning(title="Panel de Login", message="Por favor, preencha todos os campos!")
        return

    dataBaser.cursor.execute("""
        SELECT * FROM Users
        WHERE (User = ? and Password = ?)
        """, (User, Pass))

    if (not dataBaser.cursor.fetchone()):
        messagebox.showwarning(title="Painel de Login", message="Nome de Usuário ou Senha incorretos!")
        return
    
    messagebox.showinfo(title="Painel de Login", message="Login realizado com sucesso!")


LoginButton = ttk.Button(RightFrame, text="Fazer Login", width=40, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    # Escondendo botões do painel de Login
    LoginButton.place(x=1000)
    RegisterButton.place(x=1000)

    # Alterando título da janela
    jan.title("RW Project - Painel de Cadastro")

    # Exibindo campos de Cadastro
    NomeLabel = Label(RightFrame, text="Nome Completo:", font=("Century Gothic", 16), bg="#171717", fg="white")
    NomeLabel.place(x=10, y=20)

    NomeEntry = ttk.Entry(RightFrame, width=40)
    NomeEntry.place(x=220, y=25)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 16), bg="#171717", fg="white")
    EmailLabel.place(x=10, y=60)

    EmailEntry = ttk.Entry(RightFrame, width=40)
    EmailEntry.place(x=220, y=65)

    # Função de registro ao Banco de Dados
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (not Name or not Email or not User or not Pass):
            messagebox.showwarning(title="Painel de Cadastro", message="Por favor, preencha todos os campos!")
            return
        
        # Verificando se o nome de usuário já está em uso
        dataBaser.cursor.execute("""
            SELECT * FROM Users
            WHERE (User = ? and User = ?)
            """, (User, User))
        if (dataBaser.cursor.fetchone()):
            messagebox.showwarning(title="Painel de Cadastro", message="Este nome de Usuário já está em uso!")
            return

        dataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))

        dataBaser.conn.commit()

        messagebox.showinfo(title="Painel de Cadastro", message="Cadastro realizado com sucesso!")

    Register = ttk.Button(RightFrame, text="Cadastrar-se", width=40, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    # Função de retorno para o Painel de Login
    def BackToLogin():
        # Escondendo campos do painel de cadastro
        NomeLabel.place(x=1000)
        NomeEntry.place(x=1000)
        EmailLabel.place(x=1000)
        EmailEntry.place(x=1000)
        Register.place(x=1000)
        Back.place(x=1000)

        # Retornando botões do painel de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

        # Alterando título da janela
        jan.title("RW Project - Painel de Login")
    
    #Botão para retornar ao painel de Loign
    Back = ttk.Button(RightFrame, text="Fazer Login", width=30, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Cadastrar-se", width=30, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()