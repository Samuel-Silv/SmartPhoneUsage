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