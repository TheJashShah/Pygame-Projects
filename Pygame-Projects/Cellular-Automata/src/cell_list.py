from cell import Cell

def return_cell_list(WIDTH, HEIGHT, CELL_SIZE):

    cell_list = [[0] * (WIDTH//CELL_SIZE) for _ in range(HEIGHT//CELL_SIZE)]

    for i in range(HEIGHT//CELL_SIZE):
        for j in range(WIDTH//CELL_SIZE):

            cell_list[i][j] = Cell((0 + (j * 16)), (0 + (i * 16)))

    return cell_list