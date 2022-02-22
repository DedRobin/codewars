"""
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""

def valid_solution(brand):

    from itertools import chain

    pattern={1,2,3,4,5,6,7,8,9}

    #for rows

    for i in brand:
        if set(i)!=pattern:           
            return False
    
    #for columns

    for i in range(9):
        column=[x[i] for x in brand]
        if set(column)!=pattern:            
            return False

    #for sub-grids

    for i in range(0,9,3):
        temp=list(map(lambda x: x[i:i+3],brand))
        for y in range(0,9,3):
            if set(chain(*temp[y:y+3]))!=pattern:
                return False   
    return True