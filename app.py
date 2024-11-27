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