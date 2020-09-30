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
    index_line = (3 * (line_number % 3))
    index_column = (3 * (column_number % 3))
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


        #the intelignece of the programme

        break
    pass


def main():
    matrice_init= [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    solve(matrice_init)

if __name__ == '__main__':
    main()