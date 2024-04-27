import inicia_jogo_funcao as iniciar

iniciar.inicia_jogo_texto()

tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 8): '))
if tamanho_mapa < 8:
    tamanho_mapa = int(input('Tamanho do Mapa (mínimo de 8): '))

iniciar.inicia_jogo(tamanho_mapa)


"""
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

posicao = 'f8'
letra = posicao[0].upper()

linha = int(posicao[1:])
coluna = alfabeto.index(letra)

print(coluna, linha)

"""

