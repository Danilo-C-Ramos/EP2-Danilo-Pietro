import random
import suporta_posicao as sup

def aloca_navios(mapa, navios):    
    for navio in navios:
        linha = random.randint(0, len(mapa) - 1)
        coluna = random.randint(0, len(mapa) -1)
        orientacao = random.choice(['h', 'v'])

        while not sup.posicao_suporta(mapa, navio, linha, coluna, orientacao):
            linha = random.randint(0, len(mapa) - 1)
            coluna = random.randint(0, len(mapa) -1)
            orientacao = random.choice(['h', 'v'])
     
        i = 0
        while i < navio:
            if orientacao == 'h':
                mapa[linha][coluna + i] = 'N'
            elif orientacao == 'v':
                mapa[linha + i][coluna] = 'N'
            i += 1
