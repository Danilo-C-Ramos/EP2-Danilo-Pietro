from inicia_jogo import *
import random
import parametros
import suporta_posicao as sup
from detalhes import *
from verifica_vitoria import *

inicia_jogo_texto() #Printa texto introdutório

tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 6 colunas): '))

while tamanho_mapa <= 5 or tamanho_mapa > 24:
    tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 6 colunas): '))

pais_maquina = random.choice(parametros.lista_paises)
mapa_visu = cria_mapa(tamanho_mapa)

mapa_maquina, mapa_jogador, pais_jogador, frota_jogador = inicia_jogo(tamanho_mapa, pais_maquina)
#Cria um mapa para a máquina com os navios dela alocados e printa as opcoes para o jogador escolher

formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)

aloca_jogador(frota_jogador, mapa_visu, mapa_jogador, pais_maquina, pais_jogador,tamanho_mapa)

#Inicio da troca de bombas:

contagem()

atingidos_j = 0
atindios_m = 0

while not foi_derrotado(mapa_maquina) or not foi_derrotado(mapa_jogador):
    
    play = True
    while play:
        linha = random.randint(0, len(mapa_maquina) - 1)
        coluna = random.randint(0, len(mapa_maquina) - 1)
        letra = parametros.alfabeto[linha]

        if mapa_jogador[linha][coluna] == 'N':
            mapa_jogador[linha][coluna] = '\u001b[41m▒\u001b[0m'
            print(f'Computador   ---> {letra}{linha}   Navio!')
            play = False
        elif mapa_jogador[linha][coluna].strip() == '':
            mapa_jogador[linha][coluna] = '\u001b[44m▒\u001b[0m'
            print(f'Computador   ---> {letra}{linha}   Água!')
            play = False
        elif mapa_maquina[linha][coluna].strip() == 'A':
            print(f'Ja jogado, tente novamente!')
        
        formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)

        if foi_derrotado(mapa_jogador):
            vencedor = 'Computador'

    jogada = posicao_ataque()
    letra_j = jogada[0]
    linha_j = jogada[1]
    coluna_j = jogada[2]

    play_j = True
    while play_j:
        if mapa_maquina[linha_j][coluna_j].strip() == 'N':
            mapa_visu[linha_j][coluna_j] = '\u001b[41m▒\u001b[0m'
            mapa_maquina[linha_j][coluna_j] == 'X'
            print(f'Jogador   ---> {letra_j}{linha_j}   Navio!')
            play_j = False
        elif mapa_maquina[linha_j][coluna_j].strip() == '':
            mapa_visu[linha_j][coluna_j] = '\u001b[44m▒\u001b[0m'
            mapa_maquina[linha_j][coluna_j] == 'A'
            print(f'Jogador   ---> {letra_j}{linha_j}   Água!')
            play_j = False
        elif mapa_maquina[linha_j][coluna_j].strip() == 'A':
            print(f'Ja jogado, tente novamente!')
            
        
        formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)
        
        if foi_derrotado(mapa_maquina):
            vencedor = 'jogador'


print('O jogo acabou!')
print(f'O vencedor e: {vencedor}')