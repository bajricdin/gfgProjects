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


print(start_game())

