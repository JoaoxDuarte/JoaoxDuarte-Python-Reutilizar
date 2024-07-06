import requests
import time

#Criar decorator calcular_tempo
def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        print('Vou pegar a cotação')
        funcao()
        tempo_final = time.time()
        print(f'A duração foi de {tempo_final - tempo_inicial} segundos')
    return wrapper


@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()