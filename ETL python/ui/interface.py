import customtkinter as ctk

from ui.home import criar_home

ctk.set_default_color_theme("dark-blue")


def iniciar_interface():

    # Tema

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Janela

    janela = ctk.CTk()

    janela.title("ETL OLIST")

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    largura_janela = int(largura_tela * 0.85)
    altura_janela = int(altura_tela * 0.85)

    pos_x = int(
        (largura_tela - largura_janela) / 2
    )

    pos_y = int(
        (altura_tela - altura_janela) / 2
    )

    janela.geometry(
        f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}"
    )

    janela.minsize(
        1100,
        700
    )

    janela.resizable(
        True,
        True
    )

    criar_home(janela)

    janela.mainloop()