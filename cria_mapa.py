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
    mapa = N * [N * [" "]]
    return mapa
