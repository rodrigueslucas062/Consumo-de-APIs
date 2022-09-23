#Crie um código Python que consuma os dados CEPs da API Via Cep Brasil <https://viacep.com.br/>. Seu Programa deverá permitir que o usuário em uma página da web, pesquise um endereço qualquer por CEP ou nome do logradouro. Em seguida, o programa exibirá os resultados da busca em elementos <address> com o conteúdo formatado da seguinte forma:

import requests, json

cep = int(input('cep: '))

result = requests.get('https://viacep.com.br/ws'+str(cep)+'/json')
objeto =  json.load(result.text)

print(f"endereço: {objeto['logradouro']} - Bairro: {objeto['bairro']}, cidade: {objeto['localiade']}, UF: {objeto['uf']}, cep: {objeto['cep']}")