# Bibliotecas:
from ETL.extract import extrair_csv_python, dados
from ETL.validate import validar_dados, dados_validos
from ETL.transform import converter_dados, dados_transformados
from ETL.load import transformar_lista_em_csv, transformar_lista_em_json, transformar_invalidos_json, transformar_invalidos_csv

# Código principal:

extrair_csv_python()

validar_dados()

converter_dados()

transformar_lista_em_json()

transformar_lista_em_csv()

transformar_invalidos_csv()

transformar_invalidos_json()