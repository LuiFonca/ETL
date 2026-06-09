# ETL Olist E-commerce Dataset

## 📌 Sobre o Projeto

Este projeto implementa um pipeline ETL (Extract, Transform, Load) utilizando Python, Pandas e MySQL.

Os dados são provenientes do dataset público da Olist e passam pelas seguintes etapas:

1. **Extract** – Leitura dos arquivos CSV.
2. **Transform** – Tratamento, limpeza e padronização dos dados.
3. **Load** – Inserção dos dados tratados em um banco MySQL.

---

## 🛠 Tecnologias Utilizadas

* Python 3
* Pandas
* SQLAlchemy
* PyMySQL
* MySQL
* MySQL Workbench

---

## 📂 Estrutura do Projeto

```text
ETL-python/
│
├── dados/
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   └── olist_sellers_dataset.csv
│
├── extract.py
├── transform.py
├── load.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🗄 Configuração do Banco de Dados

Inicie o MySQL:

```bash
brew services start mysql
```

Acesse o MySQL:

```bash
mysql -u root
```

Crie o banco:

```sql
CREATE DATABASE olist_etl;
```

---

## 🚀 Executando o Projeto

Execute:

```bash
python3 main.py
```

O pipeline irá:

* Ler todos os CSVs
* Gerar relatório de qualidade dos dados
* Realizar transformações
* Gerar relatório pós-tratamento
* Carregar os dados para o MySQL

---

## 🔄 Transformações Aplicadas

### Customers

* Remoção de registros duplicados

### Geolocation

* Remoção de registros duplicados

### Order Items

* Conversão de datas para datetime

### Order Payments

* Validação de integridade dos dados

### Order Reviews

* Tratamento de valores nulos
* Conversão de datas para datetime

### Orders

* Conversão de datas para datetime
* Preservação de valores nulos relevantes

### Products

* Correção de nomes de colunas
* Padronização dos dados

### Sellers

* Remoção de registros duplicados

---

## 📊 Relatório de Qualidade

O sistema gera automaticamente:

* Quantidade de linhas
* Quantidade de colunas
* Registros duplicados
* Valores nulos
* Tipos de dados

Antes e depois das transformações.

---

## 🧱 Arquitetura do Pipeline

```text
CSV Files
    ↓
Extract
    ↓
Transform
    ↓
MySQL
    ↓
Power BI
```

---

## 🎯 Objetivos do Projeto

* Aplicar conceitos de ETL
* Praticar manipulação de dados com Pandas
* Trabalhar com bancos relacionais
* Desenvolver habilidades de Engenharia de Dados
* Integrar dados para análise posterior em Power BI

---

## 👨‍💻 Autor

Luiz Fonseca

Projeto desenvolvido para fins de estudo e aprendizado em Engenharia de Dados.
