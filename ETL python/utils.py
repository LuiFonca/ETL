def gerar_relatorio_dataframe(nome, df):

    texto = ""

    texto += f"\n{'=' * 70}\n"
    texto += f"TABELA: {nome}\n"
    texto += f"{'=' * 70}\n"

    texto += f"Linhas: {len(df):,}\n"
    texto += f"Colunas: {len(df.columns)}\n"
    texto += f"Duplicados: {df.duplicated().sum():,}\n"

    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]

    if len(nulos) > 0:

        texto += "\nCOLUNAS COM VALORES NULOS:\n"

        for coluna, qtd in nulos.items():

            percentual = (qtd / len(df)) * 100

            texto += (
                f"- {coluna}: "
                f"{qtd:,} registros "
                f"({percentual:.2f}%)\n"
            )

    else:

        texto += "\nNenhum valor nulo encontrado.\n"

    texto += "\nTipos das colunas:\n"
    texto += str(df.dtypes)

    texto += "\n\n"

    return texto