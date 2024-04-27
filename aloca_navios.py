"""
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
    mapa_maquina = mapa
    for blocos in navios:
        linha = random.randint(0, len(mapa) - 1)
        coluna = random.randint(0, len(mapa) - 1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa_maquina, blocos, linha, coluna, orientacao):
            linha = random.randint(0, len(mapa) - 1)
            coluna = random.randint(0, len(mapa) -1)
            orientacao = random.choice(['h', 'v'])
        
        for j in range(blocos):
            if orientacao == 'h':
                mapa_maquina[linha][(coluna + j)] = 'N'
            elif orientacao == 'v':
                mapa_maquina[linha + j][coluna] = 'N'
    return mapa_maquina
"""
import random

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
    mapa_maquina = mapa
    total_blocks = sum(navios)
    print("Total blocks:", total_blocks)
    allocated_blocks = 0
    
    for blocos in navios:
        linha = random.randint(0, len(mapa) - 1)
        coluna = random.randint(0, len(mapa[0]) - 1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa_maquina, blocos, linha, coluna, orientacao):
            linha = random.randint(0, len(mapa) - 1)
            coluna = random.randint(0, len(mapa[0]) - 1)
            orientacao = random.choice(['h', 'v'])
        
        for j in range(blocos):
            if orientacao == 'h':
                mapa_maquina[linha][coluna + j] = 'N'
            elif orientacao == 'v':
                mapa_maquina[linha + j][coluna] = 'N'

            allocated_blocks += 1
            print("Allocated blocks:", allocated_blocks)
            if allocated_blocks >= total_blocks:
                break
        if allocated_blocks >= total_blocks:
            break
    
    print("Final Map:")
    for row in mapa_maquina:
        print(' '.join(row))
    
    return mapa_maquina


# Printing initial map
print("Initial Map:")
initial_map = [['' for _ in range(10)] for _ in range(10)]
for row in initial_map:
    print(' '.join(row))

# Allocating ships
final_map = aloca_navios(initial_map, [4, 3, 3, 2, 2, 2])

# Printing final map
print("\nFinal Map:")
for row in final_map:
    print(' '.join(row))


