import customtkinter as ctk
from tkinter import messagebox
from ui.dashboard import abrir_dashboard

from main import executar_pipeline

from ui.relatorios import (
    abrir_dados_brutos,
    abrir_dados_tratados
)

from ui.mysql_view import abrir_mysql


def criar_home(janela):

    # Limpa a tela atual

    for widget in janela.winfo_children():
        widget.destroy()

    # Frame principal

    frame_principal = ctk.CTkFrame(
        janela,
        corner_radius=15
    )

    frame_principal.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    # Título

    titulo = ctk.CTkLabel(
        frame_principal,
        text="ETL OLIST",
        font=(
            "Arial",
            32,
            "bold"
        )
    )

    titulo.pack(
        pady=(25, 10),
        padx=40
    )

    subtitulo = ctk.CTkLabel(
        frame_principal,
        text="Pipeline ETL + Explorador de Dados",
        font=(
            "Arial",
            14
        )
    )

    subtitulo.pack(
        pady=(0, 20)
    )

    # Função ETL

    def executar():

        try:

            executar_pipeline()

            messagebox.showinfo(
                "Sucesso",
                "ETL executado com sucesso!"
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    largura = 320

    # Botões

    ctk.CTkButton(
        frame_principal,
        text="🚀 Executar ETL",
        width=largura,
        height=45,
        command=executar
    ).pack(pady=6)

    ctk.CTkButton(
        frame_principal,
        text="📊 Dashboard",
        width=largura,
        height=45,
        command=lambda:
            abrir_dashboard(janela)
    ).pack(pady=6)

    ctk.CTkButton(
        frame_principal,
        text="📂 Dados Brutos",
        width=largura,
        height=45,
        command=lambda:
            abrir_dados_brutos(janela)
    ).pack(pady=6)

    ctk.CTkButton(
        frame_principal,
        text="🧹 Dados Tratados",
        width=largura,
        height=45,
        command=lambda:
            abrir_dados_tratados(janela)
    ).pack(pady=6)

    ctk.CTkButton(
        frame_principal,
        text="🗄️ Explorador MySQL",
        width=largura,
        height=45,
        command=lambda:
            abrir_mysql(janela)
    ).pack(pady=6)


    ctk.CTkButton(
        frame_principal,
        text="❌ Sair",
        width=largura,
        height=45,
        fg_color="#B22222",
        hover_color="#8B0000",
        command=janela.destroy
    ).pack(
        pady=(15, 25)
    )