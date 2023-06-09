import pandas as pd
from twilio.rest import Client

# SID do twilio.com/console
account_sid = "ACf1e64c61cbc58aa0fcb013cf93b8a00c"
# Token de autenticação do twilio.com/console
auth_token = "a7b0346ed7534d61cf7c495a01df55ac"
client = Client(account_sid, auth_token)

Lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
primeiro_lugar = {'Nome': '', 'Vendas': 0}
segundo_lugar = {'Nome': '', 'Vendas': 0}
terceiro_lugar = {'Nome': '', 'Vendas': 0}
houve_vencedores = False

for mes in Lista_meses:
    Tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    vendedores_acima_55000 = Tabela_vendas.loc[Tabela_vendas['Vendas'] > 55000]

    if not vendedores_acima_55000.empty:
        houve_vencedores = True
        for _, row in vendedores_acima_55000.iterrows():
            if row['Vendas'] > primeiro_lugar['Vendas']:
                terceiro_lugar = segundo_lugar
                segundo_lugar = primeiro_lugar
                primeiro_lugar = {'Nome': row['Vendedor'], 'Vendas': row['Vendas'], 'Mês': mes}
            elif row['Vendas'] > segundo_lugar['Vendas']:
                terceiro_lugar = segundo_lugar
                segundo_lugar = {'Nome': row['Vendedor'], 'Vendas': row['Vendas'], 'Mês': mes}
            elif row['Vendas'] > terceiro_lugar['Vendas']:
                terceiro_lugar = {'Nome': row['Vendedor'], 'Vendas': row['Vendas'], 'Mês': mes}

if houve_vencedores:
    vencedores = []
    if primeiro_lugar['Nome']:
        vencedores.append(f'1º lugar: {primeiro_lugar["Nome"]} - Vendas: {primeiro_lugar["Vendas"]} - Mês: {primeiro_lugar["Mês"]}')

    if segundo_lugar['Nome']:
        vencedores.append(f'2º lugar: {segundo_lugar["Nome"]} - Vendas: {segundo_lugar["Vendas"]} - Mês: {segundo_lugar["Mês"]}')
    else:
        vencedores.append('2º lugar: Não há.')

    if terceiro_lugar['Nome']:
        vencedores.append(f'3º lugar: {terceiro_lugar["Nome"]} - Vendas: {terceiro_lugar["Vendas"]} - Mês: {terceiro_lugar["Mês"]}')
    else:
        vencedores.append('3º lugar: Não há.')

    # Unir todos os vencedores em uma única string
    mensagem = '\n'.join(vencedores)

    # Enviar mensagem como SMS
    sender_number = "+13613043410"
    recipient_number = "+5511983159106"
    message_body = mensagem
    message = client.messages.create(body=message_body, from_=sender_number, to=recipient_number)
    print("Mensagem enviada. SID:", message.sid)
else:
    print('Não há vencedores!')
