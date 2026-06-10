import tkinter as tk
from tkinter import ttk
import math

from extract import carregar_dados
from transform import (
    tratar_customers,
    tratar_geolocation,
    tratar_order_items,
    tratar_order_payments,
    tratar_order_reviews,
    tratar_orders,
    tratar_products,
    tratar_sellers
)

REGISTROS_POR_PAGINA = 50


class TelaRelatorio:

    def __init__(self, janela, tabelas):

        self.janela = janela
        self.tabelas = tabelas

        self.df_original = None
        self.df_atual = None

        self.pagina_atual = 0

        self.criar_tela()

    def criar_tela(self):

        for widget in self.janela.winfo_children():
            widget.destroy()

        self.frame = tk.Frame(self.janela)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # topo
        topo = tk.Frame(self.frame)
        topo.pack(fill="x")

        tk.Label(
            topo,
            text="Tabela:"
        ).pack(side="left")

        self.combo = ttk.Combobox(
            topo,
            values=list(self.tabelas.keys()),
            state="readonly",
            width=30
        )

        self.combo.pack(side="left", padx=10)
        self.combo.bind(
            "<<ComboboxSelected>>",
            self.carregar_tabela
        )

        # pesquisa
        tk.Label(
            topo,
            text="Pesquisar:"
        ).pack(side="left", padx=(30, 0))

        self.entry_busca = tk.Entry(
            topo,
            width=30
        )

        self.entry_busca.pack(side="left")

        tk.Button(
            topo,
            text="Buscar",
            command=self.buscar
        ).pack(side="left", padx=5)

        tk.Button(
            topo,
            text="Limpar",
            command=self.limpar_busca
        ).pack(side="left")

        # relatório
        self.relatorio = tk.Text(
            self.frame,
            height=10
        )

        self.relatorio.pack(
            fill="x",
            pady=10
        )

        # tabela
        self.tree = ttk.Treeview(
            self.frame
        )

        self.tree.pack(
            fill="both",
            expand=True
        )

        # paginação
        rodape = tk.Frame(self.frame)
        rodape.pack(fill="x", pady=10)

        self.lbl_pagina = tk.Label(
            rodape,
            text="Página 0"
        )

        self.lbl_pagina.pack(side="left")

        tk.Button(
            rodape,
            text="← Anterior",
            command=self.pagina_anterior
        ).pack(side="right")

        tk.Button(
            rodape,
            text="Próxima →",
            command=self.proxima_pagina
        ).pack(side="right", padx=5)

        # voltar
        tk.Button(
            rodape,
            text="Voltar",
            command=self.voltar
        ).pack(side="left", padx=10)

    def voltar(self):

        from ui.home import criar_home

        criar_home(self.janela)

    def carregar_tabela(self, event=None):

        nome = self.combo.get()

        self.df_original = self.tabelas[nome]
        self.df_atual = self.df_original.copy()

        self.pagina_atual = 0

        self.mostrar_relatorio()
        self.mostrar_tabela()

    def mostrar_relatorio(self):

        df = self.df_atual

        texto = ""

        texto += f"Linhas: {len(df):,}\n"
        texto += f"Colunas: {len(df.columns)}\n"
        texto += f"Duplicados: {df.duplicated().sum():,}\n\n"

        nulos = df.isnull().sum()
        nulos = nulos[nulos > 0]

        if len(nulos) == 0:
            texto += "Nenhum valor nulo encontrado."
        else:
            texto += "Valores nulos:\n"

            for coluna, qtd in nulos.items():

                percentual = (
                    qtd / len(df)
                ) * 100

                texto += (
                    f"{coluna}: "
                    f"{qtd:,} "
                    f"({percentual:.2f}%)\n"
                )

        self.relatorio.delete(
            "1.0",
            tk.END
        )

        self.relatorio.insert(
            tk.END,
            texto
        )

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
                f"de "
                f"{total_paginas}"
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

        self.mostrar_relatorio()
        self.mostrar_tabela()

    def limpar_busca(self):

        self.df_atual = (
            self.df_original.copy()
        )

        self.entry_busca.delete(
            0,
            tk.END
        )

        self.pagina_atual = 0

        self.mostrar_relatorio()
        self.mostrar_tabela()

    def proxima_pagina(self):

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

    def pagina_anterior(self):

        if self.pagina_atual > 0:

            self.pagina_atual -= 1

            self.mostrar_tabela()


def abrir_dados_brutos(janela):

    tabelas = carregar_dados()

    TelaRelatorio(
        janela,
        tabelas
    )


def abrir_dados_tratados(janela):

    tabelas = carregar_dados()

    tabelas["Customers"] = tratar_customers(
        tabelas["Customers"]
    )

    tabelas["Geolocation"] = tratar_geolocation(
        tabelas["Geolocation"]
    )

    tabelas["Order Items"] = tratar_order_items(
        tabelas["Order Items"]
    )

    tabelas["Order Payments"] = tratar_order_payments(
        tabelas["Order Payments"]
    )

    tabelas["Order Reviews"] = tratar_order_reviews(
        tabelas["Order Reviews"]
    )

    tabelas["Orders"] = tratar_orders(
        tabelas["Orders"]
    )

    tabelas["Products"] = tratar_products(
        tabelas["Products"]
    )

    tabelas["Sellers"] = tratar_sellers(
        tabelas["Sellers"]
    )

    TelaRelatorio(
        janela,
        tabelas
    )