def cria_mapa(tamanho):
    linha = []
    for i in range(tamanho):
        linha.append('' * tamanho)
    mapa = linha * tamanho
    return mapa

print(cria_mapa(10))