import pandas as pd
import openpyxl as xl
import twilio as tw

# Abrir os 6 arquivos de excel
Lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in Lista_meses:
    Tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (Tabela_vendas['Vendas'] > 55000).any():
        vendedor = Tabela_vendas.loc[Tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = Tabela_vendas.loc[Tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'O vendedor {vendedor} vendeu {vendas} no mês de {mes}, ou seja, bateu a meta de R$ 55.000,00.')

# Para cada arquivo, verificar se algum valor na coluna de vendas é maior do que R$ 55.000,00

# Se for maior do que R$ 55k, enviar SMS para meu número com nome, mes e vendas do vendedor



