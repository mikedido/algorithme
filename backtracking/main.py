import random

def display_matrice(matrice):
    """
    Display the matrice
    """
    for i in range(9):
        for j in range(9):
            print(matrice[i][j], end=' ')
        print()

def is_value_absent_column(value, column_number, matrice):
    """
    Check if the value exist in the column
    """
    for i in range(9):
        if matrice[i][column_number] == value :
            return False

    return True

    
def is_value_absent_line(value, line_number, matrice):
    """
    Check if the value exist in the line
    """
    for j in range(9):
        if matrice[line_number][j] == value :
            return False

    return True


def is_value_absent_bloc(value, line_number, column_number, matrice):
    """
    Check if the value exist in the bloc 3x3
    """
    index_line = (3 * (line_number // 3))
    index_column = (3 * (column_number // 3))
    for i in range(index_line, index_line + 3):
        for j in range(index_column, index_column + 3):
            if matrice [i][j] == value:
                return False
    return True


def get_all_value_posibilities(line_number, column_number, matrice):
    """
    Return all the values posibilities on cell
    """
    all_posible_values = []
    for value in range (1, 10):
        if (is_value_absent_bloc(value, line_number, column_number, matrice) and
        is_value_absent_column(value, column_number, matrice) and
        is_value_absent_line(value, line_number, matrice)):
            all_posible_values.append(value)

    random.shuffle(all_posible_values)

    return all_posible_values


def solve(matrice):
    finish = False
    while(not finish):
        print('step:')
        display_matrice(matrice)
        
        all_cell_posibilities=[]
        # get all the values posibilities of all the cell of the matrice
        for i in range(9):
            for j in range(9):
                if matrice[i][j] == 0 :
                    all_cell_posibilities.append([i, j, get_all_value_posibilities(i, j, matrice)])
        
        #stoped condition
        if not all_cell_posibilities:
            return matrice

        #sort the posibilities of all the cell array
        all_cell_posibilities.sort(key=lambda x: len(x[2]))

        if (len(all_cell_posibilities[0][2]) == 1):
            matrice[all_cell_posibilities[0][0]][all_cell_posibilities[0][1]] = all_cell_posibilities[0][2][0]
            continue

        #the intelignece of the programme
        matrice_tmp = matrice
        matrice_tmp[all_cell_posibilities[0][0]][all_cell_posibilities[0][1]] = all_cell_posibilities[0][2][0]
        

        if (solve(matrice_tmp)) :
            return solve(matrice_tmp)
            
        finish= True


def main():
    matrice_init= [
        [3, 0, 0, 0, 4, 8, 0, 6, 0],
        [0, 0, 0, 0, 9, 0, 4, 3, 1],
        [6, 0, 4, 3, 5, 0, 0, 2, 9],
        [9, 8, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 5, 9, 3],
        [5, 3, 0, 0, 7, 4, 9, 0, 2],
        [8, 6, 9, 0, 2, 0, 0, 0, 0],
        [0, 4, 0, 8, 1, 0, 0, 0, 6]
    ]
    solve(matrice_init)

if __name__ == '__main__':
    main()