<div align="center">

# ⚡ Pipeline ETL em Python

### Transformando dados brutos em informações validadas e organizadas.

![Python](https://img.shields.io/badge/Python-ETL-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Data%20Processing-217346?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Data%20Output-000000?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-00BFFF?style=for-the-badge)

<br>

> **Projeto prático desenvolvido para aplicar conceitos de Engenharia de Dados, utilizando Python para extrair, validar, transformar e exportar dados.**

</div>

---

#  Sobre o Projeto

Este projeto implementa um **pipeline ETL (Extract, Transform, Load)** utilizando Python.

De forma simples, o sistema recebe dados de um arquivo **CSV**, verifica se as informações estão corretas, transforma os registros válidos e separa os dados que possuem erros ou inconsistências.

O objetivo é demonstrar, na prática, como dados brutos podem ser preparados para utilização em:

- 📊 Dashboards
- 🗄️ Bancos de Dados
- 📈 Relatórios
- ☁️ Plataformas Cloud

---

#  Como funciona?

```text
         DATASET CSV
              │
              ▼
       ┌──────────────┐
       │   EXTRACT    │
       │ Extrai dados │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │   VALIDATE   │
       │ Valida dados │
       └──────┬───────┘
              │
        ┌─────┴─────┐
        ▼           ▼
   ✅ VÁLIDOS    ❌ INVÁLIDOS
        │           │
        ▼           │
   ┌───────────┐    │
   │ TRANSFORM │    │
   └─────┬─────┘    │
         │          │
         └────┬─────┘
              ▼
       ┌──────────────┐
       │     LOAD     │
       │ CSV + JSON   │
       └──────────────┘
```

---

#  Entendendo o Pipeline

##  Extract.py

A primeira etapa é responsável por ler os dados do arquivo de origem.

```text
Arquivo CSV
    ↓
Python
    ↓
Dados estruturados
```

Cada linha do arquivo é preparada para seguir para a próxima etapa do pipeline.

---

##  Validate.py

Os dados passam por verificações para identificar informações incorretas ou incompatíveis.

### Campos analisados

```text
ID
Quantity
Price
Order_Date
```

### Exemplos de validações

```text
✓ ID deve ser um número válido
✓ Quantity deve ser maior que 0
✓ Price não pode ser negativo
✓ Order_Date deve possuir um formato válido
```

Após essa etapa, os registros são separados:

```text
        DADOS
          │
          ▼
      VALIDATE
          │
     ┌────┴────┐
     ▼         ▼

  ✅ VÁLIDOS  ❌ INVÁLIDOS
```

---

##  Transform.py

Os dados válidos são convertidos e padronizados para garantir maior consistência.

### Exemplos

```text
"10"        → 10
"199.90"    → 199.90
"NOTEBOOK"  → "notebook"
```

Essa etapa prepara os dados para serem utilizados posteriormente em outros sistemas.

---

##  Load.py

Ao final do pipeline, os dados são exportados em diferentes formatos.

### Dados válidos e tratados

```text
📄 dados_tratados.csv
📦 dados_tratados.json
```

### Dados inválidos

```text
❌ dados_improprios.csv
❌ dados_improprios.json
```

---

# Estrutura do Projeto

```text
ETL/
│
├── Data/
│   │
│   ├── raw/
│   │   └── Dataset original
│   │
│   └── processed/
│       └── Dados processados
│
├── src/
│   │
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

#  Tecnologias Utilizadas

<div align="center">

<img src="https://skillicons.dev/icons?i=python,git,github,vscode" />

<br><br>

![CSV](https://img.shields.io/badge/CSV-Data%20Processing-217346?style=for-the-badge)

![JSON](https://img.shields.io/badge/JSON-Data%20Format-000000?style=for-the-badge&logo=json&logoColor=white)

</div>

Além disso, o projeto utiliza módulos nativos do Python:

```text
csv
json
datetime
```

---

#  Como Executar no seu PC

### 1. Clone o repositório

```bash
git clone https://github.com/mateusvicentevieira/ETL.git
```

### 2. Entre na pasta do projeto

```bash
cd ETL
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
python main.py
```

---

#  Conceitos Praticados

Durante o desenvolvimento deste projeto foram aplicados conceitos importantes de **Engenharia de Dados e Desenvolvimento de Software**:

- ✓ ETL
- ✓ Manipulação de arquivos CSV
- ✓ Manipulação de JSON
- ✓ Validação de dados
- ✓ Conversão de tipos
- ✓ Tratamento de exceções
- ✓ Organização de código
- ✓ Separação de responsabilidades
- ✓ Qualidade de dados
- ✓ Git e GitHub

---

#  Próximas Melhorias

- [ ] Integração com PostgreSQL
- [ ] Adicionar um mini relatório automatizado que retorna dados expecificos como: campo com maior número de dados invalidos, taxa de aproveitamento de dados...


---

#  Autor

<div align="center">

## Mateus Vicente Gonçalves

Estudante de **Engenharia de Software**, desenvolvendo conhecimentos em:

### Data Engineering • Python • SQL • Software Engineering

<a href="https://github.com/mateusvicentevieira">
  <img src="https://img.shields.io/badge/GitHub-mateusvicentevieira-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/mateusvicente">
  <img src="https://img.shields.io/badge/LinkedIn-mateusvicente-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<br><br>

---

### 🚀 Dados brutos → Validação → Transformação → Informação organizada

**Extract → Validate → Transform → Load**

</div>
