import random


def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    
    print("Commands are as follows: ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    add_new_2(mat)   
    return mat

def add_new_2(mat):
    c = random.randint(0,3)
    r = random.randint(0,3)

    while mat[r][c] != 0:
        c = random.randint(0,3)
        r = random.randint(0,3)
    
    mat[r][c] = 2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'


def compress(mat):
    changed = False

    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    for i in range(4):
        pos = 0

        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if pos != j:
                    changed = True
                pos += 1

    return new_mat, changed

def merge(mat):
    changed = False

    for i in range(4):
        for j in range(3):
            if (mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True

    return mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_left(grid):
    new_grid, changed1 = compress(grid)

    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    new_grid = compress(new_grid)

    return new_grid, changed


new_mat = [[2,2,0,0],[2,2,0,0],[2,2,0,0],[2,2,0,0]]
# print(reverse(new_mat))
print(new_mat)
print(transpose(new_mat))
# print(new_mat)
# print(merge(new_mat))
print(compress(start_game()))


