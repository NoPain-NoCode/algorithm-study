class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                sum += self.matrix[row][col]

        return sum
