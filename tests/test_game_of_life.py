import copy

class GameOfLife:
    def __init__(self, input_grid):
        self.grid = input_grid
        self.boundaries = [len(input_grid), len(input_grid[0])]

    def next_generation(self):
        next_grid = copy.deepcopy(self.grid)
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                num_alive = self.num_alive_neighbors(r, c)
                if num_alive < 2 or num_alive > 3:
                    next_grid[r][c] = 0
                if num_alive == 3:
                    next_grid[r][c] = 1

        self.grid = next_grid
        return next_grid
    
    def num_alive_neighbors(self, row, col):
        directions = [(row-1, col), (row+1,col), (row, col-1), (row, col+1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
        num_alive = 0
        for row, col in directions:
            if self.is_cell_in_bounds(row, col):
                num_alive += self.grid[row][col]
        return num_alive

    def is_cell_in_bounds(self, row, col):
        if row < 0: return False
        if row >= self.boundaries[0]: return False
        if col < 0: return False
        if col >= self.boundaries[1]: return False
        return True

def test_game_of_life_grid_dimensions():
    inputGrid = [[]]
    game = GameOfLife(inputGrid)
    result = game.next_generation()

    assert len(result) == len(inputGrid)
    assert len(result[0]) == len(inputGrid[0])
    assert len(result[-1]) == len(inputGrid[-1])

def test_num_alive_neighbors_complete_grid():
    inputGrid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    game = GameOfLife(inputGrid)
    result = game.num_alive_neighbors(1, 1)
    assert result == 8

def test_num_alive_neighbors_complete_grid_corner():
    inputGrid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    game = GameOfLife(inputGrid)
    result = game.num_alive_neighbors(0, 0)
    assert result == 3

def test_num_alive_neighbors_partial_grid():
    inputGrid = [[0, 1, 0], [1, 1, 1], [1, 0, 0]]
    game = GameOfLife(inputGrid)
    result = game.num_alive_neighbors(1, 1)
    assert result == 4

def test_is_cell_in_bounds_true():
    inputGrid = [[0, 1, 0], [1, 1, 1], [1, 0, 0]]
    game = GameOfLife(inputGrid)
    result = game.is_cell_in_bounds(1, 1)
    assert result == True

def test_is_cell_in_bounds_false():
    inputGrid = [[0, 1, 0], [1, 1, 1], [1, 0, 0]]
    game = GameOfLife(inputGrid)
    result = game.is_cell_in_bounds(4, 1)
    assert result == False

def test_game_of_life_loneliness():
    inputGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    game = GameOfLife(inputGrid)
    result = game.next_generation()
    expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    assert len(expected_result) == len(inputGrid)
    assert result == expected_result

def test_game_of_life_stasis():
    inputGrid = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    game = GameOfLife(inputGrid)
    result = game.next_generation()
    expected_result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    assert len(expected_result) == len(inputGrid)
    assert result == expected_result

