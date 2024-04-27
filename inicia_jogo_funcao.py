import paises
import random
import aloca_navios as alocar
import cria_mapa

def inicia_jogo_texto():
    print('=============================================\n|                                           |')
    print('| Design de Software INSPER - Batalha Naval |')
    print('|       Danilo Ramos e Pietro Bettega       |')
    print('|                                           |')
    print('=============================================\n')
    
    return 'Iniciando o jogo!'
 
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


#def inicia_jogo_novamente():
#    print('Iniciando o jogo novamente!')
    