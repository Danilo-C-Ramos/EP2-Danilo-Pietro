def cria_mapa(N):
    mapa = [
        [' ' for coluna in range(N + 1)] #Cria uma linha com N " ", ou seja, N colunas
             for linha in range(N + 1)] # Cria N linhas
    return mapa