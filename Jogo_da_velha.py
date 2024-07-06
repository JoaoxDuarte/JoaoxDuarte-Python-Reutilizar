import os
import random
import sys
from colorama import Fore, Back, Style

jogar_novamente = 's'
jogadas = 0
quem_joga = 2  # 2 é o jagador e 1 é a CPU
max_jogadas = 9
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# função para desenhar e limpar a tela e redesenhar.


def tela():
    global velha  # não precisa ser global
    global jogadas
    os.system('cls')

    print('    0   1   2')
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('-----------------')
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('-----------------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print('-----------------')
    # str(jogadas) por ser inteira tnenho que conv
    print('jogadas: ' + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogador_joga():
    global jogadas
    global quem_joga
    global max_jogadas
    # Verifica de quem é a vez:
    if quem_joga == 2 and jogadas < max_jogadas:  # se for vdd, posso jogar.
        try:
            l = int(input('Linha..: '))
            c = int(input('Coluna.: '))
            while velha[l][c] != ' ':
                l = int(input('Linha..: '))
                c = int(input('Coluna.: '))
            velha[l][c] = 'X'
            quem_joga = 1  # passo a vez para cpu
            jogadas += 1  # encremento as jogadas em 1
        except:
            print('Linha e/ou coluna inválida!')


# função para jogada da cpu
def cpu_joga():
    global jogadas
    global quem_joga
    global max_jogadas
    if quem_joga == 1 and jogadas < max_jogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != ' ':  # verificar se a posição está vazia
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = 'O'
        jogadas += 1
        quem_joga = 2


def verificar_vitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        # Verificar Linhas
        il = ic = 0  # É IGUAL A ic = 0
        #il = 0
        while il < 3:  # pq só tem linha 0, 1 e 2.
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != 'n'):
            break

        # Verificar COLUNAS
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0  # Para cada coluna vou prercorrer a linha
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != 'n'):
            break

        # Verificar Diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if (velha[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if (soma == 3):
            vitoria = s
            break

        # Verificar Diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if (velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quem_joga
    global max_jogadas
    global vitoria
    jogadas = 0
    quem_joga = 2  # 2 é o jagador e 1 é a CPU
    max_jogadas = 9
    velha = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


# Lupe principal
while (jogar_novamente == 's' or 'S'):
    while True:
        tela()
        # jog
        jogador_joga()
        # cpu
        cpu_joga()
        # vv
        tela()
        vitoria = verificar_vitoria()
        if (vitoria != 'n') or (jogadas >= max_jogadas):
            break



    print(Fore.RED + 'FIM DE JOGO' + Fore.YELLOW)
    if (vitoria == 'X' or vitoria == 'O'):
        print('Resultado: Jogador ' + vitoria + ' venceu!')
    else:
        print('Resultado: Empate')
    jogar_novamente = input(Fore.BLUE + 'Jogar Novamente? [s/n] ' + Fore.RESET)
    if (jogar_novamente == 'n' or 'N'):
        os.system('cls') or None
        sys.exit()

