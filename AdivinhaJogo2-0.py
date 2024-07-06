from random import randint
from time import sleep

computador = randint(0, 10)
print("-=-" * 20)
print("Vou pensar em um n° entre 0 e 10. Tente advinhar...")
print("-=-" * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    print("PROCESSANDO...")
    sleep(1)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez!')
        elif jogador > computador:
            print("Menos... tente mais uma vez.")
print(f'Acertou com {palpites} tentativas.')