#Crie um código Python que consuma os dados de moedas (currencies) da API Financeira da HG Brasil <https://hgbrasil.com/status/finance>. Seu Programa deverá ler do usuário, um valor financeiro qualquer fornecido sempre em reais (R$), e convertê-lo para Euro (EUR) e Dólares (USD); a partir dos dados fornecidos pela API. 

import requests, json

result = requests.get("https://hgbrasil.com/status/finance?key=501a1ec2")
objeto = json.loads(result.text)

dolar = objeto['result']['currencies']['USD']['buy']
euro = objeto['result']['currencies']['EUR']['buy']
real = float(input('Valor em Real: '))

print(f'Valor em Dolar: {real * dolar}\n Valor em Euro: {real * euro}' )
