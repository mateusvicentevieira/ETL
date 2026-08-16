# Importando dados validos:

from ETL.validate import dados_validos

# Constantes:

dados_transformados = []

# Classes e funções:

def converter_dados():

    for linha in dados_validos:

        linha['ID'] = int(linha['ID'])
        linha['Quantity'] = int(linha['Quantity'])
        linha['Price'] = float(linha['Price'])
        linha['Product'] = linha['Product'].lower()
        

        dados_transformados.append(linha)



     
