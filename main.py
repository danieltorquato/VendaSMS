#Pandas -> Integração do Python com excel
import pandas as pd
import openpyxl as op
from twilio.rest import Client
#openyxl -> Integração do Python com excel

#Twillio -> integração Python com SMS
# Your Account SID from twilio.com/console
account_sid = "AC80ac59655b3b676a91057a8bc8c9bc3c"
# Your Auth Token from twilio.com/console
auth_token  = "758fe87d5d5a06d6947d57338f8d32ff"
client = Client(account_sid, auth_token)
#Abrir 6 arquivos em Excel
lista_meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')


#Verificar se algum valor na coluna  Vendas é maior que R$55.000

    if (tabela_vendas["Vendas"]>55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} há um vendedor com mais de R$55.000. Vendedor: {vendedor}, Vendas:{vendas}')
#Se for maior que R$55.000 -> Envia um SMS com o Nome, Mês e vendas do vendedor
        message = client.messages.create(
            to="+5511953898557",
            from_="+17604932840",
            body=f"O Vendedor {vendedor} conseguiu bater a meta de {vendas} em vendas")

        print(message.sid)