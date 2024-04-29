def foi_derrotado(matriz):
    for i in matriz:
        if 'N' in i:
            return False
    return True

print(foi_derrotado([
    ['X', ' ', 'N'],
    ['X', 'A', 'X'],
    ['X', ' ', 'X']
]))