from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

from services.chart_service import (
    pagamentos_por_tipo,
    pedidos_por_estado
)


def grafico_pagamentos(frame):

    dados = pagamentos_por_tipo()

    fig = Figure(
        figsize=(5, 4),
        dpi=100
    )

    ax = fig.add_subplot(111)

    ax.pie(
        dados.values,
        labels=dados.index,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Formas de Pagamento"
    )

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )


def grafico_estados(frame):

    dados = pedidos_por_estado()

    fig = Figure(
        figsize=(5, 4),
        dpi=100
    )

    ax = fig.add_subplot(111)

    ax.bar(
        dados.index,
        dados.values
    )

    ax.set_title(
        "Pedidos por Estado"
    )

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )