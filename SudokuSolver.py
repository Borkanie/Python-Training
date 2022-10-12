import numpy as np
from itertools import repeat


class ElementSolution:
    def __init__(self, line: int, column: int, solutions: list):
        self.line = line
        self.column = column
        self.solutions = solutions

    def __gt__(self, object):
        return self.solutions > object.solutions

    def __sm__(self, object):
        return self.solutions < object.solutions

    def __eq__(self, object):
        return self.solutions == object.solutions

    def print(self):
        print("possible set for "+str(self.line) +
              " "+str(self.column)+":"+self.solutions)


class SudokuBoard:
    field = np.zeros((9, 9))

    def __init__(self, sudokuBoard: str):
        i = 0
        j = 0
        for letter in sudokuBoard:
            self.field[i, j] = int(letter)
            j += 1
            if (j == 9):
                i += 1
                j = 0

    def solve(self):
        solutionsInSquares = self.getPossibleSolutionsInSquares()
        solutionsInLines = self.getPossibleSolutionsInLines()
        solutionsInColumns = self.getPossibleSolutionsInColumns()
        possibleSolutions = []
        for i in range(0, 9):
            for j in range(0, 9):
                if (self.field[i, j] == 0):
                    possibleset = set(solutionsInSquares[self.indexOfCorrespondingBlock(
                        i, j)]) & set(solutionsInLines[i]) & set(solutionsInColumns[j])
                    possibleset = list(possibleset)
                    possibleSolutions.append(
                        ElementSolution(i, j, possibleset))
                    # self.field[i, j] = possibleset[0]
                    # solutionsInSquares[self.indexOfCorrespondingBlock(i,j)].remove(possibleset[0])
                    # solutionsInLines[i].remove(possibleset[0])
                    # solutionsInColumns[i].remove(possibleset[0])
                    # self.print()
                    print()
        possibleSolutions.sort()
        n = 1
        for solution in possibleSolutions:
            self.field[solution.line, solution.column] = solution.solutions[0]
            for index in range(n, len(possibleSolutions)):
                solutionToUpdate = possibleSolutions[index]
                isSameLine = solutionToUpdate.line == solution.line
                isSameColumn = solutionToUpdate.column == solution.column
                isSameSquare = self.indexOfCorrespondingBlock(solutionToUpdate.line, solutionToUpdate.column) == self.indexOfCorrespondingBlock(solution.line,solution.column)
                if (isSameLine or isSameColumn or isSameSquare):
                    if(solution.solutions[0] in solutionToUpdate.solutions):
                        solutionToUpdate.solutions.remove(solution.solutions[0])
            solution.solutions.remove(solution.solutions[0])
            n+=1

    def getPossibleSolutionsInLines(self):
        possibleSolutionsInLines = [list(range(1, 10))
                                    for i in repeat(None, 9)]
        for i in range(0, 9):
            for j in range(0, 9):
                if (int(self.field[i, j]) != 0):
                    possibleSolutionsInLines[i].remove(int(self.field[i, j]))
        return possibleSolutionsInLines

    def getPossibleSolutionsInColumns(self):
        possibleSolutionsInColumns = [
            list(range(1, 10)) for i in repeat(None, 9)]
        for j in range(0, 9):
            for i in range(0, 9):
                if (int(self.field[j, i]) != 0):
                    possibleSolutionsInColumns[i].remove(int(self.field[j, i]))
        return possibleSolutionsInColumns

    def getPossibleSolutionsInSquares(self):
        possibleSolutionsInSquare = [
            list(range(1, 10)) for i in repeat(None, 9)]
        for i in range(0, 9):
            for j in range(0, 9):
                if (int(self.field[i, j]) != 0):
                    possibleSolutionsInSquare[self.indexOfCorrespondingBlock(
                        i, j)].remove(int(self.field[i, j]))
        return possibleSolutionsInSquare

    def print(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if (j % 3 == 2 and j < 8):
                    print(str(self.field[i, j])+" ", end='|')
                else:
                    print(str(self.field[i, j])+" ", end=' ')
            if (i % 3 == 2 and i < 8):
                print("\n-------------------------------------------")
            else:
                print("")

    def indexOfCorrespondingBlock(self, line: int, column: int) -> int:
        return 3*int(line/3)+int(column/3) % 3


def main():
    sudoku = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
    board = SudokuBoard(sudoku)
    board.print()
    board.solve()


if __name__ == "__main__":
    main()
