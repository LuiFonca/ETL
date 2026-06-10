import tkinter as tk
from tkinter import messagebox
from ui.mysql_view import abrir_mysql

from main import executar_pipeline

from ui.relatorios import (
    abrir_dados_brutos,
    abrir_dados_tratados
)

from ui.mysql_view import abrir_mysql



def criar_home(janela):

    for widget in janela.winfo_children():
        widget.destroy()

    frame = tk.Frame(janela)

    frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    titulo = tk.Label(
        frame,
        text="ETL OLIST",
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=20)


    # BOTÕES

    tk.Button(
        frame,
        text="Dados Brutos",
        width=30,
        height=2,
        command=lambda:
            abrir_dados_brutos(janela)
    ).pack(pady=5)

    tk.Button(
        frame,
        text="Dados Tratados",
        width=30,
        height=2,
        command=lambda:
            abrir_dados_tratados(janela)
    ).pack(pady=5)

    tk.Button(
    frame,
    text="Explorar MySQL",
    width=30,
    height=2,
    command=lambda:
        abrir_mysql(janela)
    ).pack(pady=5)

    def executar():

        try:

            executar_pipeline()

            messagebox.showinfo(
                "Sucesso",
                "ETL executado com sucesso."
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    tk.Button(
        frame,
        text="Executar ETL",
        width=30,
        height=2,
        command=executar
    ).pack(pady=5)

    tk.Button(
        frame,
        text="Sair",
        width=30,
        height=2,
        command=janela.destroy
    ).pack(pady=5)
