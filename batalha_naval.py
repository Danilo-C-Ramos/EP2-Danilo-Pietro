from inicia_jogo import *
import random
import parametros
import suporta_posicao as sup
from detalhes import *
from verifica_vitoria import *

inicia_jogo_texto() #Printa texto introdutório

tamanho_mapa_in = input('Tamanho do Mapa (mínimo de 6 colunas): ')

certo = True
while not tamanho_mapa_in.isdigit() or certo:
    if tamanho_mapa_in.isdigit():
        if not int(tamanho_mapa_in) <= 5 and not int(tamanho_mapa_in) > 27:
            tamanho_mapa = int(tamanho_mapa_in)
            certo = False
    if not tamanho_mapa_in.isdigit() or certo:
        tamanho_mapa_in = input('Tamanho do Mapa (mínimo de 6 colunas): ')
    
     

pais_maquina = random.choice(parametros.lista_paises)
mapa_visu = cria_mapa(tamanho_mapa)

mapa_maquina, mapa_jogador, pais_jogador, frota_jogador = inicia_jogo(tamanho_mapa, pais_maquina)
#Cria um mapa para a máquina com os navios dela alocados e printa as opcoes para o jogador escolher

formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)

aloca_jogador(frota_jogador, mapa_visu, mapa_jogador, pais_maquina, pais_jogador,tamanho_mapa)

#Inicio da troca de bombas:

contagem()
jogo_terminou = False

while not jogo_terminou:
    play = True
    while play:
        linha = random.randint(1, len(mapa_maquina)) - 1
        coluna = random.randint(1, len(mapa_maquina)) - 1
        letra = parametros.alfabeto[coluna]

        while mapa_jogador[linha][coluna].strip() == 'A' or mapa_jogador[linha][coluna].strip() == 'X':
            print(f'Ja jogado, tente novamente!')
            linha = random.randint(1, len(mapa_maquina)) - 1
            coluna = random.randint(1, len(mapa_maquina)) - 1
            letra = parametros.alfabeto[coluna]
            
        if mapa_jogador[linha][coluna] == '\u001b[42m│▒│\u001b[0m':
            mapa_jogador[linha][coluna] = '\u001b[41m│▒│\u001b[0m'
            print(f'Computador   ---> {letra}{linha + 1}   Navio!')
            print()
            play = False
        elif mapa_jogador[linha][coluna].strip() == '':
            mapa_jogador[linha][coluna] = '\u001b[44m▒▒▒\u001b[0m'
            print(f'Computador   ---> {letra}{linha+ 1}   Água!')
            print()
            play = False
        
        
        formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)

    if foi_derrotado(mapa_jogador):
        vencedor = 'Computador'
        jogo_terminou = True
        break

    jogada = posicao_ataque(tamanho_mapa)
    letra_j = jogada[0]
    linha_j = jogada[1]
    coluna_j = jogada[2]

    play_j = True
    while play_j:
        while mapa_maquina[linha_j][coluna_j].strip() == 'A' or mapa_maquina[linha_j][coluna_j].strip() == 'X':
            print(f'Ja jogado, tente novamente!')
            jogada = posicao_ataque(tamanho_mapa)
            letra_j = jogada[0]
            linha_j = jogada[1]
            coluna_j = jogada[2]
        if mapa_maquina[linha_j][coluna_j].strip() == 'N':
            mapa_visu[linha_j][coluna_j] = '\u001b[41m│▒│\u001b[0m'
            mapa_maquina[linha_j][coluna_j] = 'X'
            print(f'Jogador   ---> {letra_j}{linha_j + 1}   Navio!')
            play_j = False
        elif mapa_maquina[linha_j][coluna_j].strip() == '':
            mapa_visu[linha_j][coluna_j] = '\u001b[44m▒▒▒\u001b[0m'
            mapa_maquina[linha_j][coluna_j] = 'A'
            print(f'Jogador   ---> {letra_j}{linha_j + 1}   Água!')
            play_j = False

        time.sleep(0.5)   
        
        formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)
        
    if foi_derrotado(mapa_maquina):
        vencedor = 'jogador'
        jogo_terminou = True
        break

print('O jogo acabou!')
print(f'O vencedor é: {vencedor}')