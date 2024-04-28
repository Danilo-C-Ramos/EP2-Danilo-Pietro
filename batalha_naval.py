import inicia_jogo_funcao as iniciar
import random
import parametros

iniciar.inicia_jogo_texto() #Printa texto introdutório

tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 5 colunas): '))

pais_maquina = random.choice(parametros.lista_paises)

mapa_maquina, mapa_jogador, pais_jogador, frota_jogador = iniciar.inicia_jogo(tamanho_mapa, pais_maquina)
#Cria um mapa para a máquina com os navios dela alocados e printa as opcoes para o jogador escolher

iniciar.printa_mapa(mapa_jogador, pais_maquina, pais_jogador)

"""
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

posicao = 'f8'
letra = posicao[0].upper()

linha = int(posicao[1:])
coluna = alfabeto.index(letra)

print(coluna, linha)

"""

