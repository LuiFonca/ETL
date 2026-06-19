import customtkinter as ctk

from ui.charts import (
    grafico_pagamentos,
    grafico_estados
)

from services.dashboard_service import (
    total_clientes,
    total_pedidos,
    total_produtos,
    total_vendedores,
    valor_total_vendido,
    ticket_medio,
    nota_media_reviews,
    pagamento_mais_utilizado
)




def criar_card(parent, titulo, valor):

    card = ctk.CTkFrame(
        parent,
        width=220,
        height=120,
        corner_radius=12
    )

    card.pack(
        side="left",
        expand=True,
        fill="both",
        padx=10,
        pady=10
    )

    ctk.CTkLabel(
        card,
        text=titulo,
        font=("Arial", 16, "bold")
    ).pack(
        pady=(15, 5)
    )

    ctk.CTkLabel(
        card,
        text=str(valor),
        font=("Arial", 24)
    ).pack(
        pady=(0, 15)
    )

    return card


def abrir_dashboard(janela):

    for widget in janela.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(
        janela,
        corner_radius=15
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    titulo = ctk.CTkLabel(
        frame,
        text="📊 Dashboard OLIST",
        font=("Arial", 28, "bold")
    )

    titulo.pack(
        pady=20
    )

    # PRIMEIRA LINHA

    cards_superiores = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    cards_superiores.pack(
        fill="x",
        padx=20,
        pady=10
    )

    criar_card(
        cards_superiores,
        "Clientes",
        f"{total_clientes():,}"
    )

    criar_card(
        cards_superiores,
        "Pedidos",
        f"{total_pedidos():,}"
    )

    criar_card(
        cards_superiores,
        "Produtos",
        f"{total_produtos():,}"
    )

    criar_card(
        cards_superiores,
        "Vendedores",
        f"{total_vendedores():,}"
    )

    # SEGUNDA LINHA

    indicadores = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    indicadores.pack(
        fill="x",
        padx=20,
        pady=10
    )

    criar_card(
        indicadores,
        "Valor Total",
        f"R$ {valor_total_vendido():,.2f}"
    )

    criar_card(
        indicadores,
        "Ticket Médio",
        f"R$ {ticket_medio():,.2f}"
    )

    criar_card(
        indicadores,
        "Nota Média",
        nota_media_reviews()
    )

    criar_card(
        indicadores,
        "Pagamento Líder",
        pagamento_mais_utilizado()
    )

    graficos = ctk.CTkFrame(
    frame
)

    graficos.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    grafico_pagamentos(graficos)

    grafico_estados(graficos)

    # BOTÃO VOLTAR

    def voltar():

        from ui.home import criar_home

        criar_home(janela)


      
    ctk.CTkButton(
        frame,
        text="← Voltar",
        width=180,
        height=40,
        command=voltar
    ).pack(
        pady=25
    )