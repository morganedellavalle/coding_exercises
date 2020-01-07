import sys
import random 
import time

sizes = {'Beginner': {'height': 9, 'width': 9},
        'Intermediate': {'height': 16, 'width': 16}, 
        'Expert': {'height': 30, 'width': 16}
        }

mines = {'Beginner': 10, 
        'Intermediate': 40, 
        'Expert': 99}

game_status = 'in progress'

class Board:
    def __init__(self, level):
        self.level = level
        self.width = sizes[level]['width']
        self.height = sizes[level]['height']
        self.mines = mines[level]
        self.board_content = [['-' for i in range(self.width)] for j in range(self.height)]

    def place_mines(self):
        mine_locations = random.sample(range(self.width*self.height), self.mines)
        for mine in mine_locations:
            row = mine // self.width
            col = mine % self.width
            self.board_content[row][col] = 'x'

    def number_adjacent_mines(self, row, col):
        counter = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                try:
                    if self.board_content[i][j] == 'x':
                        print(i, j)
                        counter += 1
                except IndexError:
                    pass
        return counter
    
    def pretty_print(self):
        for i in range(self.height):
            print(*self.board_content[i], sep = " ")


class Game:
    def __init__(self, level):
        #initiate real board & place mines randomly
        self.real_board = Board(level)
        self.real_board.place_mines()

        self.player_board = Board(level)

        self.status = "in progress"

        self.safe_cells_left_to_find = self.real_board.width*self.real_board.height - self.real_board.mines
        self.not_discovered_cells = [*range(self.real_board.width*self.real_board.height)]
        
    
    def play_random_move(self):
        picked_cell = random.choice(self.not_discovered_cells)
        print(picked_cell)
        self.not_discovered_cells.remove(picked_cell)
        row = picked_cell // self.real_board.width
        col = picked_cell % self.real_board.width
        self.update_board(row, col)

    def player_move(self):
        row = int(input("Enter the row # of the cell you want to sweep: "))
        col = int(input("Enter the column # of the cell you want to sweep: "))
        mine_marker = input("Mine? y/n: ")

        self.not_discovered_cells.remove(row*self.real_board.width + col)
        
        if mine_marker == 'y':
            self.player_board.board_content[row][col] = 'x'
        else:
            self.update_board(row, col)

    def update_board(self, row, col):  
        if self.real_board.board_content[row][col] == 'x':
            self.status = 'lost'
        else:
            self.player_board.board_content[row][col] = self.real_board.number_adjacent_mines(row, col)
            self.player_board.pretty_print()
            self.safe_cells_left_to_find -= 1
            if self.safe_cells_left_to_find == 0:
                self.status == 'won'
            print(self.safe_cells_left_to_find)

def main(level):
    #sanity check
    assert (level in ['Beginner', 'Intermediate', 'Expert']), "Select valid level! (Beginner, Intermediate, Expert)"

    #Initiate game
    game = Game(level)
    game.real_board.pretty_print()
    moves = 1

    while game.status == 'in progress':
        print("Move: " + str(moves))
        game.player_move()
        moves +=1
        time.sleep(1)
        
    if game.status == 'won':
        print('You won in %s moves' % moves)
    elif game.status == 'lost':
        print('You suck!!')

if __name__ == '__main__':
    main(sys.argv[1])