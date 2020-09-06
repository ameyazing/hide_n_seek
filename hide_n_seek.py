"""
run the program as:
$ python3 hide_n_seek.py

Characters:
    0 --> Blank
    1 --> Car
    2 --> Plane
    3 --> Tiger
    4 --> Boy
    5 --> Tent

Board positions:
    +-------+
    |1     2|
    |   0   |
    |4     3|
    +-------+
So the resultant array for each quadrant:
    [0 -> center; 1 -> top-left, 2 -> top-right, 3 -> bottom-right, 4 -> bottom-left]

Piece:
    0/1 at index 0 represents if center is visible or not. Value 0 indicates not visible.
    [0, 0, 1, 0, 1]
    [1, 0, 1, 0, 0]
    [0, 1, 1, 0, 0]
    [0, 1, 0, 0, 0]
"""

def generate_permutations(a):
    """
    This program will take any iterable object
    as input and will return a generator object
    as output which can be used with for 
    loop to get all the permutations
    """
    n = len(a)
    c = [0]*n
    A = list(a)
    yield A
    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                temp = A[0]
                A[0] = A[i]
                A[i] = temp
            else:
                temp = A[c[i]]
                A[c[i]] = A[i]
                A[i] = temp
            yield A
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

def get_puzzle_characters():
    print("1 = Car")
    print("2 = Plane")
    print("3 = Tiger")
    print("4 = Boy")
    print("5 = Tent")
    print("Enter the puzzle with comma separated values.")
    print("E.g.: for 2 boys, 1 tent and 1 tiger, enter the values as: 4,4,5,3")
    puzzle = input("Puzzle: ")
    puzzle = sorted(puzzle)
    puzzle = [int(x) for x in puzzle if x != ',']
    return puzzle

def match(board, pieces, puzzle):
    puzzle = sorted(puzzle)
    pieces = list(pieces)

    opencharacters = []
    for x in range(4): #for 4 pieces
        for y in range(5): #for 5 positions in the quadrant
            if pieces[x][y] == 1 and board[x][y] != 0:
                opencharacters.append(board[x][y])

    opencharacters = sorted(opencharacters)

    if opencharacters == puzzle:
        return True
    else:
        return False

def create_board_pieces():
    board = [[0, 1, 1, 5, 2], [4, 0, 5, 2, 3], [2, 1, 4, 3, 0], [3, 4, 2, 2, 0]]
    piece1 = [[1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [1, 1, 0, 0, 0]]
    piece2 = [[0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 1, 0]]
    piece3 = [[0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 0, 0, 1]]
    piece4 = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    pieces = []
    pieces.append(piece1)
    pieces.append(piece2)
    pieces.append(piece3)
    pieces.append(piece4)
    return board, pieces

def find_piece_placement(board, puzzle, piece_perm_gen):
    final_perm_list = []
    for perm in piece_perm_gen:
        for q0 in range(4):
            for q1 in range(4):
                for q2 in range(4):
                    for q3 in range(4):
                        item = (pieces[perm[0]][q0], pieces[perm[1]][q1], pieces[perm[2]][q2], pieces[perm[3]][q3])
                        res = match(board, item, puzzle)
                        if res == True:
                            print("Piece1: ", item[0])
                            print("Piece2: ", item[1])
                            print("Piece3: ", item[2])
                            print("Piece4: ", item[3])
                            return True
    return False

board, pieces = create_board_pieces()
puzzle = get_puzzle_characters()
piece_perm_gen = generate_permutations([0,1,2,3])
res = find_piece_placement(board, puzzle, piece_perm_gen)
if res == False:
    print("No solution found")
