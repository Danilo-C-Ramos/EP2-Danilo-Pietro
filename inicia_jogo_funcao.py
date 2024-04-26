import paises
import random
import aloca_navios as alocar
import cria_mapa

def inicia_jogo():
    print('=============================================\n|                                           |')
    print('| Design de Software INSPER - Batalha Naval |')
    print('|       Danilo Ramos e Pietro Bettega       |')
    print('|                                           |')
    print('=============================================\n')
    print('Iniciando o jogo!')
    
    pais_maquina = random.choice(paises.lista_paises)
    mapa = cria_mapa.cria_mapa()
    alocar.aloca_navios(mapa, paises.paises[pais_maquina])

    i = 1
    for pais, navios in paises.paises.items():
        print(f'{i}:', pais)
        for navio, quantidade in navios.items():
            print(f'   {quantidade} {navio}')
        print('')
        i += 1
    return 

def inicia_jogo_novamente():
    print('Iniciando o jogo novamente!')
    