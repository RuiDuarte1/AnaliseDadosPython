#Análise de Dados#
#Tratamento de Dados#
#Gráficos#

#--Código executado no jupyter--#

#Importando base de dados
import pandas as pd
import plotly.express as px
# !pip install plotly
tabela = pd.read_csv(r'C:\Users\ruyfl\Downloads\telecom_users.csv')

#Excluindo coluna sem utilidade e visualizando tabela
tabela = tabela.drop('Unnamed: 0', axis = 1)
display(tabela)

#Tratamento de Dados: transformando valores que estão reconhecidos de forma errada
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors = 'coerce')

#Excluindo colunas vazias
#axis: 0 -> linha, 1 -> coluna
tabela = tabela.dropna(how = 'all', axis = 1)
tabela = tabela.dropna(how = 'any', axis = 0)

#Exibindo informações do arquivo importado
#print(tabela.info())

#Análise inicial
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize = True))

#Análise Completa
#Criando e exibindo os gráficos
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color = 'Churn', text_auto = True)
    grafico.show()