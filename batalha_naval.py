import inicia_jogo as iniciar
import random
import parametros
import suporta_posicao as sup
from detalhes import *
from verifica_vitoria import *

iniciar.inicia_jogo_texto() #Printa texto introdutório

tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 6 colunas): '))

while tamanho_mapa <= 5 or tamanho_mapa > 24:
    tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 6 colunas): '))

pais_maquina = random.choice(parametros.lista_paises)


mapa_maquina, mapa_jogador, pais_jogador, frota_jogador = iniciar.inicia_jogo(tamanho_mapa, pais_maquina)
#Cria um mapa para a máquina com os navios dela alocados e printa as opcoes para o jogador escolher

iniciar.printa_mapa(tamanho_mapa, mapa_jogador, pais_maquina, pais_jogador)


iniciar.aloca_jogador(frota_jogador, tamanho_mapa, mapa_jogador, pais_maquina, pais_jogador)

#Inicio da troca de bombas:

contagem()

atingidos_j = 0
atindios_m = 0

while not foi_derrotado:
    
    play = True
    while play:
        linha = random.randint(0, len(mapa_maquina) - 1)
        coluna = random.randint(0, len(mapa_maquina) - 1)
        orientacao = random.choice(['h', 'v'])

        if mapa_jogador[linha][coluna] == 'N':
            mapa_jogador[linha][coluna] = 'X'
            print(f'Computador   ---> {linha}{coluna}   Navio!')
            play = False
        elif mapa_jogador[linha][coluna] == '':
            mapa_jogador[linha][coluna] = 'A'
            print(f'Computador   ---> {linha}{coluna}   Água!')
            play = False
        





