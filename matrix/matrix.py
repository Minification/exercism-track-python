from typing import List

Vector = List[int]

class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.rows = [
        	[int(number) for number in line.split()]
        	for line in matrix_string.splitlines()
        ]

    def row(self, index: int) -> Vector:
        return [value for value in self.rows[index-1]]

    def column(self, index: int) -> Vector:
        return [row[index-1] for row in self.rows]
