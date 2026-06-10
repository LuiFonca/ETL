import tkinter as tk

from ui.home import criar_home


def iniciar_interface():

    janela = tk.Tk()

    janela.title("ETL OLIST")

    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()

    janela.geometry(
    f"{int(largura * 0.85)}x{int(altura * 0.85)}"
)

    janela.minsize(
        1000,
        700
    )
    janela.geometry("1200x700")

    janela.resizable(True, True)

    criar_home(janela)

    janela.mainloop()