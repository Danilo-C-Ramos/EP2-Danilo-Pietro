import random
#import suporta_posicao as sup
def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    if orientacao.strip().lower() == 'v':
        final = linha + blocos
        i = linha
        if final > len(mapa):
            return False
        else:
            while i < final:
                if mapa[i][coluna].strip() != '':
                    return False
                i += 1
    elif orientacao.strip().lower() == 'h':
        final = coluna + blocos 
        i = coluna
        if final > len(mapa[0]):
            return False
        else:
            while i < final:
                if mapa[linha][i].strip() != '':
                    return False
                i += 1
    return True

def aloca_navios(mapa, navios):  
    for blocos in navios:
        linha = random.randint(0, len(mapa) - 1)
        coluna = random.randint(0, len(mapa) - 1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa, blocos, linha, coluna, orientacao):
            linha = random.randint(0, len(mapa) - 1)
            coluna = random.randint(0, len(mapa) -1)
            orientacao = random.choice(['h', 'v'])
        
        for j in range(blocos):
            if orientacao == 'h':
                mapa[linha][(coluna + j)] = 'N'
            elif orientacao == 'v':
                mapa[linha + j][coluna] = 'N'
    return
