import paises
import random
import aloca_navios as alocar
import cria_mapa
import random

def inicia_jogo(N):
    pais_maquina = random.choice(paises.lista_paises)
    print("Selected country:", pais_maquina)
    mapa = cria_mapa.cria_mapa(N)
    print("Initial Map:")
    for row in mapa:
        print(' '.join(row))
    alocar.aloca_navios(mapa, paises.blocos[pais_maquina])
    print("Final Map:")
    for row in mapa:
        print(' '.join(row))
    return

print('=============================================\n|                                           |')
print('| Design de Software INSPER - Batalha Naval |')
print('|       Danilo Ramos e Pietro Bettega       |')
print('|                                           |')
print('=============================================\n')
print('Iniciando o jogo!')

tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 8): '))
if tamanho_mapa < 8:
    tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 8): '))

inicia_jogo(tamanho_mapa)


"""
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

posicao = 'f8'
letra = posicao[0].upper()

linha = int(posicao[1:])
coluna = alfabeto.index(letra)

print(coluna, linha)

"""

