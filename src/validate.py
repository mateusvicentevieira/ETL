# Importar bibliotecas:
import datetime

# Puxando o extract.py:
from ETL.extract import dados

# Constantes:

dados_validos = []
dados_invalidos = []

# Classes e funções:

def validar_dados():

    for linha in dados:

        try:

            id = int(linha['ID'])
            quantity = int(linha['Quantity'])
            price = float(linha['Price'])
            order_date = datetime.datetime.strptime(linha['Order_Date'], '%m/%d/%Y').date()

            if (

                id > 0
                and price >= 0
                and quantity > 0

            ):
                dados_validos.append(linha)

            else:
                dados_invalidos.append(linha)

        except ValueError:
            dados_invalidos.append(linha)




