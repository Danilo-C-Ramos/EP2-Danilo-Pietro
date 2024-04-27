"""
def cria_mapa(N):
    lisf=[]
    lis=[]
    for i in range(N):
        lis.append('')
        for j in range (len(lis)):
            lisf.append(lis)
    return lisf
"""
def cria_mapa(N):
    mapa = [
        [' ' for coluna in range(N)] #Cria uma linha com N " ", ou seja, N colunas
             for linha in range(N)] # Cria N linhas
    return mapa
