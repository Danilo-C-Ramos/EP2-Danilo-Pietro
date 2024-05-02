def foi_derrotado(matriz):
    for i in matriz:
        if 'N' in i or '\u001b[42m│▒│\u001b[0m' in i:
            return False
    return True