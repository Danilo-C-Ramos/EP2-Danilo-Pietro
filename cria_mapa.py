def cria_mapa(N):
    mapa = [
        [' ' for coluna in range(N)] #Cria uma linha com N " ", ou seja, N colunas
             for linha in range(N)] # Cria N linhas
    return mapa