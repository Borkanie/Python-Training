import numpy as np
from itertools import repeat
 
class SudokuBoard:
    field=np.zeros((9,9))
    def __init__(self,sudokuBoard:str):
        i = 0
        j = 0
        for letter in sudokuBoard:
            self.field[i,j] = int(letter)
            j += 1
            if(j == 9):
                i += 1
                j = 0

    def solve(self):
        solutionsInSquares=self.getPossibleSolutionsInSquares()
        solutionsInLines=self.getPossibleSolutionsInLines()
        solutionsInColumns=self.getPossibleSolutionsInColumns()
        for i in range(0,9):
            for j in range(0,9):
                if(self.field[i,j]!=0):
                    possibleset= set(solutionsInSquares[self.indexOfCorrespondingBlock(i,j)]) & set(solutionsInLines[i]) & set(solutionsInColumns[j])
                    possibleset = list(possibleset)
                    if(len(possibleset)>0):
                        self.field[i,j] = possibleset[0]
                        solutionsInSquares[self.indexOfCorrespondingBlock(i,j)].remove(possibleset[0])
                        solutionsInLines[i].remove(possibleset[0])
                        solutionsInColumns[i].remove(possibleset[0])
                        self.print()
                        print("\n")

        
    def getPossibleSolutionsInLines(self):
        possibleSolutionsInLines=[list(range(1,10)) for i in repeat(None, 9)]
        for i in range(0,9):
            for j in range(0,9):
                if(int(self.field[i,j])!=0):
                    possibleSolutionsInLines[self.indexOfCorrespondingBlock(i,j)].remove(int(self.field[i,j]))
        return possibleSolutionsInLines

    def getPossibleSolutionsInColumns(self):
        possibleSolutionsInColumns=[list(range(1,10)) for i in repeat(None, 9)]
        for j in range(0,9):
            for i in range(0,9):
                if(int(self.field[i,j])!=0):
                    possibleSolutionsInColumns[self.indexOfCorrespondingBlock(i,j)].remove(int(self.field[i,j]))
        return possibleSolutionsInColumns

    def getPossibleSolutionsInSquares(self):
        possibleSolutionsInSquare=[list(range(1,10)) for i in repeat(None, 9)]
        for i in range(0,9):
            for j in range(0,9):
                if(int(self.field[i,j])!=0):
                    possibleSolutionsInSquare[self.indexOfCorrespondingBlock(i,j)].remove(int(self.field[i,j]))
        return possibleSolutionsInSquare

    def print(self):
        for i in range(0,9):
            for j  in range(0,9):
                if(j%3==2 and j<8):
                    print(str(self.field[i,j])+" ",end = '|')
                else:
                    print(str(self.field[i,j])+" ",end = ' ')
            if(i%3==2 and i<8):
                print("\n-------------------------------------------")
            else:
                print("")

    def indexOfCorrespondingBlock(self,line:int,column:int)->int:
        return 3*int(line/3)+int(column/3)%3


def main():
    sudoku = "004006079000000602056092300078061030509000406020540890007410920105000000840600100";
    board=SudokuBoard(sudoku)
    board.print()
    board.solve()

if __name__=="__main__":
    main()