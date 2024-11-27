# Equipe: Time do Vinishow


## Tema: SmartPhoneUsage - A utilização de Smartphones e o comportamento de usuários

## Componentes dos grupo:
- Gustavo Justino
- Neoaquison Conceição Medeiros
- Rafael Medeiros dos Santos
- Samuel Silva
- Vinicius Soares

## Links
- [Repositóiro GitHub](https://github.com/Samuel-Silv/SmartPhoneUsage)
- [Dataset Kaggle](https://www.kaggle.com/datasets/bhadramohit/smartphone-usage-and-behavioral-dataset)


## Contextualização:
O uso intenso de celulares influencia o comportamento dos usuários, afetando desde a comunicação até a saúde mental. 
A conectividade constante traz benefícios, mas também desafios para o equilíbrio pessoal e social.

![image](https://github.com/user-attachments/assets/f2c0dcc9-8d45-410b-b827-41a81772c610)

## Problema a ser resolvido:
O objetivo de nosso projeto é desenvolver uma aplicação capaz de analisar dados públicos, oferecendo insights valiosos para explicar 
como o uso de celulares transforma nossos comportamentos no âmbito social.


## Visualizações a serem geradas:
1. *Gráficos de Linha*
2. *Mapas de Calor (Heatmaps)*
3. *Gráficos de Barras e Colunas*
4. *Diagramas de Dispersão (Scatter Plots)*
5. *Nuvens de Palavras (Word Clouds)*
6. *Gráficos de Área e Radar*


## Bibliotecas e Frameworks que devem ser utilizados:

Utilizaremos uma virtualenv e as lib listadas no arquivo [requirements.txt](./requirements.txt)

1. instale o Virtualenv e crie uma virtualenv com o comando abaixo:

```` bash
python3 -m venv .venv
````

2. Instale os pacotes do arquivo [requirements.txt](./requirements.txt)

```` bash
pip install -r requirements.txt
````

3. Run App
```` bash
streamlit run app.py
````

2. Processo de obtenção dos dados

- Utilizamos um dataset do [Kaggle]("https://www.kaggle.com/datasets/bhadramohit/smartphone-usage-and-behavioral-dataset") Insights sobre o Engajamento dos Usuários e Padrões de Uso de Aplicativos em Diferentes Faixas Etárias

- Este conjunto de dados fornece insights sobre os padrões diários de uso móvel de 1.000 usuários, abrangendo aspectos como tempo de tela, uso de aplicativos e engajamento dos usuários em diferentes categorias de aplicativos.

- Inclui uma gama diversificada de usuários com base em idade, gênero e localização.

- Os dados focam no uso total de aplicativos, tempo gasto em redes sociais, aplicativos de produtividade e jogos, além do tempo total de tela.

- Essas informações são valiosas para entender tendências comportamentais e preferências de uso de aplicativos, sendo úteis para desenvolvedores de aplicativos, profissionais de marketing e pesquisadores de UX.

- Este conjunto de dados é útil para analisar o engajamento móvel, os hábitos de uso de aplicativos e o impacto de fatores demográficos no comportamento móvel. Ele pode ajudar a identificar tendências para marketing, desenvolvimento de aplicativos e otimização da experiência do usuário.

3. Script para obtenção do dataset

```` python
import os
import json
import zipfile

def download_dataset(dataset_name):
    command = f"kaggle datasets download -d {dataset_name}"
    try:
        os.system(command)
    except Exception as e:
        print(f"Falha ao tentar realizar o download: {e}")
    print('dowload zip realizado')

def unzip_file(dataset_name, zip_path, extract_to='./ingestion'):
    download_dataset(dataset_name)
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except FileNotFoundError as e:
        print(f"Erro ao extrair o csv: {e}")
    print('csv extraido')


dataset_name = "bhadramohit/smartphone-usage-and-behavioral-dataset"
z_file = 'smartphone-usage-and-behavioral-dataset.zip'
csv_file = './ingestion/mobile_usage_behavioral_analysis.csv'

unzip_file(dataset_name, z_file)

````

4. Script para criação dos dataset das analises

```` python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./ingestion/mobile_usage_behavioral_analysis.csv")

print(df.head())
print(df.columns)


# 1. Distribuição da Idade dos Usuários

dist_idade = df[
    ['Social_Media_Usage_Hours',
    'Age']
    ]
print(dist_idade.head())

sns.histplot(data=dist_idade, x='Age', bins=10)
plt.xlabel('Idade')
plt.ylabel('Número de Usuários')
plt.title('Distribuição da Idade dos Usuários')
plt.show()


# 2. Análise por tipo de aplicativo

tipo_aplicativo = df[
    ['Social_Media_Usage_Hours',
    'Productivity_App_Usage_Hours', 
    'Gaming_App_Usage_Hours', 
    'Age', 
    'Gender', 
    'Location']
    ]

print(tipo_aplicativo.head())

# Calcular a média de tempo de uso por categoria de aplicativo para cada gênero
media_tempo_por_genero = tipo_aplicativo.groupby('Gender')[
    ['Social_Media_Usage_Hours', 'Productivity_App_Usage_Hours', 'Gaming_App_Usage_Hours']
].mean()

print("Média de horas de uso por categoria de aplicativo e gênero:")
print(media_tempo_por_genero)

# Calcular a média de tempo de uso por categoria de aplicativo para cada localização
media_tempo_por_localizacao = tipo_aplicativo.groupby('Location')[
    ['Social_Media_Usage_Hours', 'Productivity_App_Usage_Hours', 'Gaming_App_Usage_Hours']
].mean()

print("\nMédia de horas de uso por categoria de aplicativo e localização:")
print(media_tempo_por_localizacao)

# 3. Comportamento de Uso

comportamentos = df[
    ['Number_of_Apps_Used', 
     'Total_App_Usage_Hours', 
     'Social_Media_Usage_Hours', 
     'Daily_Screen_Time_Hours']
    ]

print(comportamentos.head())

# 4. Insights Demográficos

geograficos = df[
    ['Location', 
     'Total_App_Usage_Hours', 
     'Daily_Screen_Time_Hours', 
     'Social_Media_Usage_Hours', 
     'Productivity_App_Usage_Hours', 
     'Gaming_App_Usage_Hours']
    ]
print(geograficos.head())

sns.boxplot(data=geograficos, x='Location', y='Daily_Screen_Time_Hours')
plt.xlabel('Localização')
plt.ylabel('Tempo de Tela Diário (Horas)')
plt.title('Distribuição de Uso de Tela Diário por Localização')
plt.xticks(rotation=45)
plt.show()




faixa_etaria = df[
    ['Age', 
    'Total_App_Usage_Hours', 
    'Daily_Screen_Time_Hours', 
    'Social_Media_Usage_Hours', 
    'Productivity_App_Usage_Hours', 
    'Gaming_App_Usage_Hours']
    ]
print(faixa_etaria.head())

# 5. Segmentação de usuários

segmentacao = df[
    ['Number_of_Apps_Used', 
    'Total_App_Usage_Hours', 
    'Social_Media_Usage_Hours', 
    'Productivity_App_Usage_Hours', 
    'Gaming_App_Usage_Hours']
    ]
print(segmentacao.head())

perfil_usuarios = df[
    ['Total_App_Usage_Hours']
    ]

print(perfil_usuarios.head())

# Seleção das colunas relevantes
segmentacao = df[
    ['Number_of_Apps_Used', 
     'Total_App_Usage_Hours', 
     'Social_Media_Usage_Hours', 
     'Productivity_App_Usage_Hours', 
     'Gaming_App_Usage_Hours']
    ]


segmentacao['User_Type'] = segmentacao['Total_App_Usage_Hours'].apply(lambda x: 'Heavy User' if x > 5 else 'Light User')

print(segmentacao.head())

print(segmentacao['User_Type'].value_counts())

# 6. Tendências e Anomalias

tendencias = df[
    ['Total_App_Usage_Hours', 
     'Daily_Screen_Time_Hours', 
     'Number_of_Apps_Used']
    ]
print(tendencias.head())

outliers = df[
    ['Total_App_Usage_Hours', 
    'Daily_Screen_Time_Hours']
    ]
print(outliers.head())

````

5. Aplicativo Streamlit

```` python

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Devop Mackenzie", page_icon="📈")

st.markdown("# Engenharia de Dados - Mackenzie")
st.markdown("## Mobile Usage Behavioral Analysis")
st.sidebar.header("Gráficos")
st.write(
    """Abaixo temos os gráficos das nossas analises"""
)

df = pd.read_csv("./ingestion/mobile_usage_behavioral_analysis.csv")
dist_idade = df[
    ['Social_Media_Usage_Hours',
    'Age']
    ]

# Configuração do índice para evitar erro de tipo
dist_idade.set_index("Age", inplace=True)

# Plotar no Streamlit
st.title("Gráfico de Barras - Social Media Usage Hours vs. Age")
st.bar_chart(dist_idade["Social_Media_Usage_Hours"])



tipo_aplicativo = df[
    ['Social_Media_Usage_Hours',
    'Productivity_App_Usage_Hours', 
    'Gaming_App_Usage_Hours', 
    'Age', 
    'Gender', 
    'Location']
    ]

print(tipo_aplicativo.head())

# Calcular a média de tempo de uso por categoria de aplicativo para cada gênero
media_tempo_por_genero = tipo_aplicativo.groupby('Gender')[
    ['Social_Media_Usage_Hours', 'Productivity_App_Usage_Hours', 'Gaming_App_Usage_Hours']
].mean()


# Plotar o gráfico de barras agrupado
fig, ax = plt.subplots(figsize=(8, 6))
media_tempo_por_genero.plot(kind='bar', ax=ax, colormap='viridis')
ax.set_title("Média de Tempo de Uso por Categoria de Aplicativo e Gênero")
ax.set_xlabel("Gênero")
ax.set_ylabel("Média de Tempo de Uso (Horas)")
ax.legend(title="Categoria de Aplicativo", bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar o layout
plt.tight_layout()

# Exibir o gráfico no Streamlit
st.title("Média de Tempo de Uso por Categoria de Aplicativo para cada Gênero")
st.pyplot(fig)


geograficos = df[
    ['Location', 
     'Total_App_Usage_Hours', 
     'Daily_Screen_Time_Hours', 
     'Social_Media_Usage_Hours', 
     'Productivity_App_Usage_Hours', 
     'Gaming_App_Usage_Hours']
]

# Configuração do Streamlit
st.title("Distribuição de Uso de Tela Diário por Localização")

# Criar o gráfico com Seaborn
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(data=geograficos, x='Location', y='Daily_Screen_Time_Hours', ax=ax)
ax.set_xlabel('Localização')
ax.set_ylabel('Tempo de Tela Diário (Horas)')
ax.set_title('Distribuição de Uso de Tela Diário por Localização')
plt.xticks(rotation=45)

# Exibir o gráfico no Streamlit
st.pyplot(fig)

````