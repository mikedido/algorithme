"""
Display matrice
"""
def display_matrice(matrice, dimension):
    for i in range(dimension):
        for j in range(dimension):
            print(matrice[i][j], end=' ')
        print()

"""
Check if the matrice is magic
"""
def matrice_is_magic(matrice, dimension):
    for i in range(dimension):
        for j in range(dimension):
            if (matrice[i][j] == 0):
                return False
    return True

"""
Init matrice
"""
def init_matrice(dimension):
    matrice = []
    for i in range(dimension):
        matrice.append([0] * dimension)
    return matrice

"""
Get indice of line and column
"""
def get_indice(matrice, i, j, dimension):
    if(matrice[(i+1)%dimension][(j+1)%dimension]==0):
        return (i+1)%dimension, (j+1)%dimension
    else:
        return (i-1)%dimension, j

"""
Main program
"""
def main():
    #init matrice
    matrice_dimension=3
    matrice_magic = init_matrice(matrice_dimension)
    #init variables
    step=1
    value=1
    no_complete=True
    indice_i=matrice_dimension-1
    indice_j=(matrice_dimension//2 + 1 ) - 1
    while no_complete:
        print('Etape : {} '.format(step))
        matrice_magic[indice_i][indice_j]= value
        display_matrice(matrice_magic, matrice_dimension)
        #condition d'arrêt ou pas
        if (matrice_is_magic(matrice_magic, matrice_dimension)):
            no_complete=False
        else:
            value+=1
            step+=1
            indice_i, indice_j = get_indice(matrice_magic, indice_i, indice_j, matrice_dimension)
    pass

if __name__ =='__main__':
    main()