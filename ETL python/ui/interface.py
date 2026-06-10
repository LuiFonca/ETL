import tkinter as tk

from ui.home import criar_home


def iniciar_interface():

    janela = tk.Tk()

    janela.title("ETL OLIST")

    janela.geometry("600x400")

    janela.resizable(False, False)

    criar_home(janela)

    janela.mainloop()