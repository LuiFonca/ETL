import tkinter as tk
from tkinter import ttk
import math

from mysql_explorer import (
    listar_tabelas,
    carregar_tabela_mysql
)

REGISTROS_POR_PAGINA = 120


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

        frame_principal = tk.Frame(self.janela)
        frame_principal.pack(
            fill="both",
            expand=True
        )

        titulo = tk.Label(
            frame_principal,
            text="Explorador MySQL",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        topo = tk.Frame(frame_principal)
        topo.pack(pady=10)

        tk.Label(
            topo,
            text="Tabela:"
        ).pack(side="left")

        self.combo = ttk.Combobox(
            topo,
            values=listar_tabelas(),
            width=30,
            state="readonly"
        )

        self.combo.pack(
            side="left",
            padx=10
        )

        self.combo.bind(
            "<<ComboboxSelected>>",
            self.carregar_tabela
        )

        self.info = tk.Label(
            frame_principal,
            text=""
        )

        self.info.pack()

        pesquisa_frame = tk.Frame(
            frame_principal
        )

        pesquisa_frame.pack(
            pady=10
        )

        tk.Label(
            pesquisa_frame,
            text="Pesquisar:"
        ).pack(side="left")

        self.entry_busca = tk.Entry(
            pesquisa_frame,
            width=30
        )

        self.entry_busca.pack(
            side="left",
            padx=5
        )

        self.entry_busca.bind(
            "<Return>",
            lambda event:
            self.buscar()
        )

        tk.Button(
            pesquisa_frame,
            text="Buscar",
            command=self.buscar
        ).pack(side="left")

        tk.Button(
            pesquisa_frame,
            text="Limpar",
            command=self.limpar
        ).pack(
            side="left",
            padx=5
        )

        tree_frame = tk.Frame(
            frame_principal
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

        scroll_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical"
        )

        scroll_x = ttk.Scrollbar(
            tree_frame,
            orient="horizontal"
        )

        self.tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(
            command=self.tree.yview
        )

        scroll_x.config(
            command=self.tree.xview
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        tree_frame.grid_rowconfigure(
            0, weight=1
        )
        tree_frame.grid_columnconfigure(
            0, weight=1
        )

        scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        rodape = tk.Frame(
            frame_principal
        )

        rodape.pack(
            pady=10
        )

        tk.Button(
            rodape,
            text="← Anterior",
            command=self.anterior
        ).pack(
            side="left",
            padx=5
        )

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
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            rodape,
            text="Voltar ao Menu",
            command=self.voltar
        ).pack(
            side="left",
            padx=20
        )

    def voltar(self):

        from ui.home import criar_home

        criar_home(
            self.janela
        )

    def carregar_tabela(
        self,
        event=None
    ):

        tabela = self.combo.get()

        self.df_original = (
            carregar_tabela_mysql(
                tabela
            )
        )

        self.df_atual = (
            self.df_original.copy()
        )

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

        self.tree["columns"] = (
            list(
                pagina.columns
            )
        )

        self.tree["show"] = (
            "headings"
        )

        for coluna in pagina.columns:

            self.tree.heading(
                coluna,
                text=coluna
            )

            self.tree.column(
                coluna,
                width=150,
                stretch=True
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
                len(df)
                /
                REGISTROS_POR_PAGINA
            )
        )

        self.lbl_pagina.config(
            text=
            f"Página {self.pagina_atual + 1} de {total_paginas}"
        )

        self.info.config(
            text=
            f"{len(df):,} registros encontrados"
        )

    def buscar(self):

        if (
            self.df_original is None
        ):
            return

        termo = (
            self.entry_busca
            .get()
            .strip()
        )

        if termo == "":
            return

        self.df_atual = (
            self.df_original[
                self.df_original
                .astype(str)
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
        )

        self.pagina_atual = 0

        self.mostrar_tabela()

    def limpar(self):

        if (
            self.df_original is None
        ):
            return

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

        if (
            self.df_atual is None
        ):
            return

        total_paginas = math.ceil(
            len(self.df_atual)
            /
            REGISTROS_POR_PAGINA
        )

        if (
            self.pagina_atual + 1
            < total_paginas
        ):

            self.pagina_atual += 1

            self.mostrar_tabela()

    def anterior(self):

        if (
            self.pagina_atual > 0
        ):

            self.pagina_atual -= 1

            self.mostrar_tabela()


def abrir_mysql(janela):

    TelaMySQL(janela)