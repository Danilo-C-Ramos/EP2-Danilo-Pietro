def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    if orientacao.strip() == 'v':
        final = (linha) + blocos
        i = linha
        if final > len(mapa):
            return False
        else:
            while i < final:
                if mapa[i][coluna].strip() != '':
                    return False
                i += 1
    elif orientacao.strip() == 'h':
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