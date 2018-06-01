import sys

class Field:
    
    def __init__(self, value):
        if value != 0:
            self.values = [value]
        else:
            self.values = [n for n in range(1,10)]

class Sudoku:

    def __init__(self, sudoku_string):
        self.sudoku = self.parse_sudoku_string(sudoku_string)

    def parse_sudoku_string(self, sudoku_string):
        sudoku = []
        for i in range(81):
            if i % 9 == 0:
                sudoku.append([Field(sudoku_string[i])])
            else:
                sudoku[i // 9] += [Field(sudoku_string[i])]
        
        return sudoku

    def reduce_possibilities(self):
        pass


def main():
    s = Sudoku(sys.argv[1])

if __name__ == "__main__":
    main()