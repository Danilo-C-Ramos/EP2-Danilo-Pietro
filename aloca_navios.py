import random
import suporta_posicao as sup

def aloca_navios(mapa, navios):  
    mapa_maquina = mapa
    for blocos in navios:
        linha = random.randint(0, len(mapa_maquina) - 1)
        coluna = random.randint(0, len(mapa_maquina) - 1)
        orientacao = random.choice(['h', 'v'])

        while not sup.posicao_suporta(mapa_maquina, blocos, linha, coluna, orientacao):
            linha = random.randint(0, len(mapa_maquina) - 1)
            coluna = random.randint(0, len(mapa_maquina) -1)
            orientacao = random.choice(['h', 'v'])
        
        for j in range(blocos):
            if orientacao == 'h':
                mapa_maquina[linha][coluna + j] = 'N'
            elif orientacao == 'v':
                mapa_maquina[linha + j][coluna] = 'N'
    return mapa_maquina



