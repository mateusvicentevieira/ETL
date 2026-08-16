# Bibliotecas:

import csv

# Constantes:

dados = []

# Classes e funções:

# Para abrir o dataset:

def extrair_csv_python():
    with open(r'C:\Users\DELL\Desktop\Data Study\Projeto ETL\Dados\e-commerce_dataset.csv','r') as dataset:
        leitura_csv = csv.DictReader(dataset)

        for linha in leitura_csv:
            dados.append(linha)



