import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from extract import carregar_dados
from main import executar_pipeline
from utils import gerar_relatorio_dataframe

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


# =====================
# FUNÇÕES AUXILIARES
# =====================

def mostrar_texto(texto):

    area_resultados.delete(
        "1.0",
        tk.END
    )

    area_resultados.insert(
        tk.END,
        texto
    )


# =====================
# EXECUTAR ETL
# =====================

def executar_etl():

    try:

        executar_pipeline()

        messagebox.showinfo(
            "Sucesso",
            "Pipeline ETL executado com sucesso!"
        )

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            str(erro)
        )


# =====================
# RELATÓRIO BRUTO
# =====================

def relatorio_bruto():

    tabelas = carregar_dados()

    texto = ""

    for nome, df in tabelas.items():

        texto += gerar_relatorio_dataframe(
            nome,
            df
        )

    mostrar_texto(texto)


# =====================
# RELATÓRIO TRATADO
# =====================

def relatorio_tratado():

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

    texto = ""

    for nome, df in tabelas.items():

        texto += gerar_relatorio_dataframe(
            nome,
            df
        )

    mostrar_texto(texto)


# =====================
# BUSCA
# =====================

def pesquisar():

    termo = entrada_busca.get().strip()

    if not termo:

        messagebox.showwarning(
            "Aviso",
            "Digite um termo para pesquisar."
        )

        return

    tabelas = carregar_dados()

    resultado = ""

    for nome, df in tabelas.items():

        filtro = df[
            df.astype(str)
            .apply(
                lambda coluna:
                coluna.str.contains(
                    termo,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

        if len(filtro) > 0:

            resultado += (
                f"\n{'=' * 70}\n"
                f"{nome}\n"
                f"{'=' * 70}\n"
            )

            resultado += (
                filtro.head(20)
                .to_string()
            )

            resultado += "\n\n"

    if resultado == "":

        resultado = (
            f"Nenhum registro encontrado para: {termo}"
        )

    mostrar_texto(resultado)


# =====================
# JANELA
# =====================

janela = tk.Tk()

janela.title("ETL Olist")
janela.geometry("500x400")

# =====================
# MENU ESQUERDO
# =====================

frame_botoes = tk.Frame(
    janela,
    padx=10,
    pady=10
)

frame_botoes.pack(
    side=tk.LEFT,
    fill=tk.Y
)

titulo = tk.Label(
    frame_botoes,
    text="ETL OLIST",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=10)

# =====================
# BOTÕES
# =====================

btn_etl = tk.Button(
    frame_botoes,
    text="Executar ETL",
    width=25,
    height=2,
    command=executar_etl
)

btn_etl.pack(pady=5)

btn_relatorio_bruto = tk.Button(
    frame_botoes,
    text="Relatório Bruto",
    width=25,
    height=2,
    command=relatorio_bruto
)

btn_relatorio_bruto.pack(pady=5)

btn_relatorio_tratado = tk.Button(
    frame_botoes,
    text="Relatório Tratado",
    width=25,
    height=2,
    command=relatorio_tratado
)

btn_relatorio_tratado.pack(pady=5)

# =====================
# PESQUISA
# =====================

label_busca = tk.Label(
    frame_botoes,
    text="Pesquisar:"
)

label_busca.pack(pady=(20, 5))

entrada_busca = tk.Entry(
    frame_botoes,
    width=30
)

entrada_busca.pack()

btn_busca = tk.Button(
    frame_botoes,
    text="Buscar",
    width=25,
    height=2,
    command=pesquisar
)

btn_busca.pack(pady=5)

# =====================
# ÁREA DE RESULTADOS
# =====================

area_resultados = ScrolledText(
    janela,
    width=150,
    height=50
)

area_resultados.pack(
    side=tk.RIGHT,
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=10
)

janela.mainloop()