# Importar bibliotecas:

from ETL.transform import dados_transformados
from ETL.validate import dados_invalidos
import csv, json

# Classes e funções:

# Carregamento dos dados tratados:

def transformar_lista_em_json():

    with open('dados_tratados.json','w') as dados_tratados:
        json.dump(dados_transformados, dados_tratados, indent=4)

def transformar_lista_em_csv():

    with open('dados_tratados.csv','w',newline='', encoding='utf-8') as dados_tratados:

        colunas = dados_transformados[0].keys()

        escrever = csv.DictWriter(dados_tratados, fieldnames=colunas)

        escrever.writeheader()

        escrever.writerows(dados_transformados)

# Carregamento dos dados inválidos:

def transformar_invalidos_json():

    with open('dados_improprios.json', 'w') as dados_improprios:
        json.dump(dados_invalidos, dados_improprios, indent=4)

def transformar_invalidos_csv():

    with open('dados_improprios.csv', 'w') as dados_csv:

        colunas = dados_invalidos[0].keys()

        escrever = csv.DictWriter(dados_csv, fieldnames=colunas)

        escrever.writeheader()

        escrever.writerows(dados_invalidos)

