
def foi_derrotado(matriz):
    for i in matriz:
        for j in i:
            if j == "N":
                return False
    return True

print(foi_derrotado([
    ['X', ' ', 'N'],
    ['X', 'A', 'X'],
    ['X', ' ', 'X']
]))