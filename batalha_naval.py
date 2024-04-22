alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

posicao = 'f8'
letra = posicao[0].upper()

linha = int(posicao[1:])
coluna = alfabeto.index(letra)

print(coluna, linha)