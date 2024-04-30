import parametros
import random
import aloca_navios as alocar
from detalhes import *

def cria_mapa(N):
    mapa = [
        [' ' for coluna in range(N + 1)] #Cria uma linha com N " ", ou seja, N colunas
             for linha in range(N + 1)] # Cria N linhas
    return mapa

def inicia_jogo_texto():
    print('=============================================\n|                                           |')
    print('| Design de Software INSPER - Batalha Naval |')
    print('|       Danilo Ramos e Pietro Bettega       |')
    print('|                                           |')
    print('=============================================\n')
    
    return
 
def inicia_jogo(N, pais_maquina):
    print('Iniciando o jogo!')

    print(f'Computador está alocando a frota do país: {pais_maquina}...')
    loading()

    mapa_jogador = cria_mapa(N)
    mapa_maquina = cria_mapa(N)
    mapa_maquina = alocar.aloca_navios(mapa_maquina, parametros.blocos[pais_maquina])
    
    c = 1
    for pais, navios in parametros.paises.items():
        print(f'{c}: {pais}')
        c += 1
        for navio, quantidade in navios.items():
            print(f'    {navio}: {quantidade}')
        
    numero = int(input('Qual o nomero do seu país? ')) - 1
    pais_jogador = parametros.lista_paises[numero]
    frota_jogador = parametros.paises[pais_jogador]

    return mapa_maquina, mapa_jogador, pais_jogador, frota_jogador

def printa_mapa(mapa, pais_maquina, pais_jogador):
    linha = 1
    espaco = len(f'{linha} {mapa[linha]} {linha}') - len(f'Computador: {pais_maquina}') + 1 
     #Espaco variável para printar o nome do pais do Jogador

    print(f'Computador: {pais_maquina}', f' ' * espaco, f'Jogador: {pais_jogador}')
     #Printa o país da máquina e o país do jogador em cima dos mapas
    
    #lista_black = [('     ' * len(mapa))] * len(mapa[0])
    

    while linha < len(mapa):
        print(f'{linha}', f'{mapa[linha]}', f'{linha}', f'{linha}', f'{mapa[linha]}', f'{linha}')
        
        linha += 1
     
    return mapa





#def inicia_jogo_novamente():
#    print('Iniciando o jogo novamente!')