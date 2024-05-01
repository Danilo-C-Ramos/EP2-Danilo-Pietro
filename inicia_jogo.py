import parametros
import aloca_navios as alocar
from detalhes import *
import suporta_posicao as sup
from cria_mapa import *
import time

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


def printa_mapa(mapa_visu, mapa, pais_maquina, pais_jogador):
    linha = 1
    espaco = len(f'{linha} {mapa[linha]} {linha}') - len(f'Computador: {pais_maquina}') + 1 
     #Espaco variável para printar o nome do pais do Jogador

    print(f'Computador: {pais_maquina}', f' ' * espaco, f'Jogador: {pais_jogador}')
     #Printa o país da máquina e o país do jogador em cima dos mapas
    
    #lista_black = [('     ' * len(mapa))] * len(mapa[0])
    

    while linha < len(mapa):
        print(f'{linha}', f'{mapa_visu[linha]}', f'{linha}', f'{linha}', f'{mapa[linha]}', f'{linha}')
        
        linha += 1
    return mapa


def aloca_jogador(frota, mapa_visu, mapa_jogador, pais_maquina, pais_jogador, tamanho_mapa):
    for navio in frota:
        blocos = parametros.CONFIGURACAO[navio]
        
        print('alocar: ', navio, f'({blocos} blocos)')
        print('Próximos: ', navio, '\n')
        
        posicao = input('Digite a posicao (coordenada): ')

        t = len(posicao) >= 2

        if posicao[0].isalpha() and t:
            letra = posicao[0].upper()
            f = True
        else:
            f = False
        
        if t:
            numero = posicao[1]
        else:
            numero = ''
        
        if numero.isdigit() and t:
            linha = int(posicao[1])
            f = True
        else:
            linha = 0
            f = False
        
        if t:
            coluna = parametros.alfabeto.index(letra)
        else:
            coluna = 0

        io = input('Orientação (h/v): ')
        
        if io.lower() == 'h' or io.lower() == 'v':
            orientacao = io.lower()
            o = True
        else:
            o = False

        while not sup.posicao_suporta(mapa_jogador, blocos, linha, coluna, orientacao) or not f or not o or not t:
            print('Posicao não disponível! Tente novamente...')
            posicao = input('Digite a posicao (coordenada): ')

            t = len(posicao) >= 2

            if posicao[0].isalpha() and t:
                letra = posicao[0].upper()
                f = True
            else:
                f = False
            
            if t:
                numero = posicao[1]
            else:
                numero = ''
            
            if numero.isdigit() and t:
                linha = int(posicao[1])
                f = True
            else:
                linha = 0
                f = False
            
            if t:
                coluna = parametros.alfabeto.index(letra)
            else:
                coluna = 0

            io = input('Orientação (h/v): ')
            
            if io.lower() == 'h' or io.lower() == 'v':
                orientacao = io.lower()
                o = True
            else:
                o = False

        for bloco in range(parametros.CONFIGURACAO[navio]): #Alocando o navio
            if orientacao == 'v':
                mapa_jogador[linha + bloco][coluna] = '\u001b[42m▒\u001b[0m'
            elif orientacao == 'h':
                mapa_jogador[linha][coluna + bloco] = '\u001b[42m▒\u001b[0m'
        
        time.sleep(0.3)

        print('Navio alocado!\n')
        formata_mapa(mapa_visu, mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador)
    
    return ''


def posicao_ataque():
    posicao = input('Digite a posicao (coordenada): ')

    t = len(posicao) >= 2

    if posicao[0].isalpha() and t:
        letra = posicao[0].upper()
        f = True
    else:
        f = False
        
    if t:
        numero = posicao[1]
    else:
        numero = ''
        
    if numero.isdigit() and t:
        linha = int(posicao[1])
        f = True
    else:
        linha = 0
        f = False
        
    if t:
        coluna = parametros.alfabeto.index(letra)
    else:
        coluna = 0


    while not f or not t:
            posicao = input('Digite a posicao (coordenada): ')

            t = len(posicao) >= 2

            if posicao[0].isalpha() and t:
                letra = posicao[0].upper()
                f = True
            else:
                f = False
            
            if t:
                numero = posicao[1]
            else:
                numero = ''
            
            if numero.isdigit() and t:
                linha = int(posicao[1])
                f = True
            else:
                linha = 0
                f = False
            
            if t:
                coluna = parametros.alfabeto.index(letra)
            else:
                coluna = 0

    return letra, linha, coluna

def formata_mapa(mapa_visu,mapa_jogador, tamanho_mapa, pais_maquina, pais_jogador):  
    lista_letras = parametros.alfabeto_virgula[: (tamanho_mapa * 2) - 1].split(',')
    
    espaco = tamanho_mapa * 3 + 8 - len(f'Computador: {pais_maquina}')
     #Espaco variável para printar o nome do pais do Jogador

    print(f'Computador: {pais_maquina}', f' ' * espaco, f'Jogador: {pais_jogador}' )
     #Printa o país da máquina e o país do jogador em cima dos mapas

    print(' ', end = ' ')
    for letra in lista_letras:
        print(letra, end = '  ')
    print('      ', end = '')
    for letra in lista_letras:
        print(letra, end = '  ')
    
    linha = 1
    #for i in range(len(mapa_visu)):
    #    mapa_visu[i].insert(0, linha)
    #    mapa_visu[i].insert(len(mapa_visu) + 1, linha)
    #    mapa_jogador[i].insert(0, linha)
    #    mapa_jogador[i].insert(len(mapa_visu) + 1, linha)
    #    linha += 1
    
    c = 0
    for linha in range(len(mapa_visu)):
        print()
        print(linha, end = '')
        for valor in mapa_visu[linha]:
            print(valor, end = '  ')
        
        print(linha, end = '    ')
        print(linha, end = '')
        for valor in mapa_jogador[linha]:
            print(valor, end = '  ')
        
        print(linha, end = '')
        c += 1
    print()
    
    print(' ', end = ' ')
    for letra in lista_letras:
        print(letra, end = '  ')
    print('      ', end = '')
    for letra in lista_letras:
        print(letra, end = '  ')
    print('\n')

    return

print('Thominhas', end = ' ')
print('Arroz')