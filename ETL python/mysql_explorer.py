import tkinter as tk
from tkinter import ttk
import math

from mysql_explorer import (
    listar_tabelas,
    carregar_tabela_mysql
)

REGISTROS_POR_PAGINA = 50


class TelaMySQL:

    def __init__(self, janela):

        self.janela = janela

        self.df_original = None
        self.df_atual = None

        self.pagina_atual = 0

        self.criar_tela()

    def criar_tela(self):

        for widget in self.janela.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.janela)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        titulo = tk.Label(
            frame,
            text="Explorador MySQL",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=10)

        topo = tk.Frame(frame)
        topo.pack(fill="x")

        tk.Label(
            topo,
            text="Tabela:"
        ).pack(side="left")

        self.combo = ttk.Combobox(
            topo,
            values=listar_tabelas(),
            state="readonly",
            width=30
        )

        self.combo.pack(
            side="left",
            padx=10
        )

        self.combo.bind(
            "<<ComboboxSelected>>",
            self.carregar_tabela
        )

        tk.Label(
            topo,
            text="Pesquisar:"
        ).pack(
            side="left",
            padx=(20, 0)
        )

        self.entry_busca = tk.Entry(
            topo,
            width=30
        )

        self.entry_busca.pack(
            side="left"
        )

        tk.Button(
            topo,
            text="Buscar",
            command=self.buscar
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            topo,
            text="Limpar",
            command=self.limpar
        ).pack(
            side="left"
        )

        self.info = tk.Label(
            frame,
            text=""
        )

        self.info.pack(
            pady=5
        )

        self.tree = ttk.Treeview(frame)

        self.tree.pack(
            fill="both",
            expand=True
        )

        rodape = tk.Frame(frame)
        rodape.pack(
            fill="x",
            pady=10
        )

        tk.Button(
            rodape,
            text="← Anterior",
            command=self.anterior
        ).pack(side="left")

        self.lbl_pagina = tk.Label(
            rodape,
            text="Página 1"
        )

        self.lbl_pagina.pack(
            side="left",
            padx=10
        )

        tk.Button(
            rodape,
            text="Próxima →",
            command=self.proxima
        ).pack(side="left")

        tk.Button(
            rodape,
            text="Voltar",
            command=self.voltar
        ).pack(side="right")

    def voltar(self):

        from ui.home import criar_home

        criar_home(self.janela)

    def carregar_tabela(self, event=None):

        tabela = self.combo.get()

        self.df_original = carregar_tabela_mysql(
            tabela
        )

        self.df_atual = self.df_original.copy()

        self.pagina_atual = 0

        self.mostrar_tabela()

    def mostrar_tabela(self):

        self.tree.delete(
            *self.tree.get_children()
        )

        df = self.df_atual

        inicio = (
            self.pagina_atual *
            REGISTROS_POR_PAGINA
        )

        fim = (
            inicio +
            REGISTROS_POR_PAGINA
        )

        pagina = df.iloc[
            inicio:fim
        ]

        self.tree["columns"] = list(
            pagina.columns
        )

        self.tree["show"] = "headings"

        for coluna in pagina.columns:

            self.tree.heading(
                coluna,
                text=coluna
            )

            self.tree.column(
                coluna,
                width=120
            )

        for _, linha in pagina.iterrows():

            self.tree.insert(
                "",
                tk.END,
                values=list(linha)
            )

        total_paginas = max(
            1,
            math.ceil(
                len(df) /
                REGISTROS_POR_PAGINA
            )
        )

        self.lbl_pagina.config(
            text=(
                f"Página "
                f"{self.pagina_atual + 1} "
                f" de "
                f"{total_paginas}"
            )
        )

        self.info.config(
            text=(
                f"{len(df):,} registros encontrados"
            )
        )

    def buscar(self):

        termo = self.entry_busca.get()

        if not termo:
            return

        self.df_atual = self.df_original[
            self.df_original.astype(str)
            .apply(
                lambda x:
                x.str.contains(
                    termo,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

        self.pagina_atual = 0

        self.mostrar_tabela()

    def limpar(self):

        self.df_atual = (
            self.df_original.copy()
        )

        self.entry_busca.delete(
            0,
            tk.END
        )

        self.pagina_atual = 0

        self.mostrar_tabela()

    def proxima(self):

        total_paginas = math.ceil(
            len(self.df_atual)
            / REGISTROS_POR_PAGINA
        )

        if (
            self.pagina_atual + 1
            < total_paginas
        ):

            self.pagina_atual += 1

            self.mostrar_tabela()

    def anterior(self):

        if self.pagina_atual > 0:

            self.pagina_atual -= 1

            self.mostrar_tabela()


def abrir_mysql(janela):

    TelaMySQL(janela)