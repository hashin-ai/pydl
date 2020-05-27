import random


class Matrix:
    def __init__(self, rows, cols, default_values):
        self.rows = rows
        self.cols = cols
        self.shape = (rows, cols)
        if default_values == "r":  # Generate a matrix of random values
            self.values = [
                [round(random.random(), 3) for i in range(self.rows)]
                for j in range(self.cols)
            ]
        elif default_values == "i":  # Generate identity matrix
            if rows != cols:  # Identity matrices have to be square
                print(
                    f"Shape error: You cannot create a non square identity matrix!\nDefaulting to matrix of 0's!"
                )
                self.values = [
                    [0] * cols for val in range(rows)
                ]  # Create a matrix of zeros instead
            else:
                # Indexing by rows here is arbitrary since identity matrices rows == cols ALWAYS
                self.values = [[0 for i in range(rows)] for j in range(rows)]
                for i in range(0, rows):
                    self[(i, i)] = 1
        else:
            self.values = [[default_values] * cols for val in range(rows)]

    def __str__(self):
        return "\n".join(map(str, [value for value in self.values]))

    def __getitem__(self, indices):
        i, j = indices
        return self.values[i][j]

    def __setitem__(self, indices, value):
        i, j = indices
        self.values[i][j] = value
        return self.values

    def __add__(self, other):
        if self.shape != other.shape:
            print(
                f"Shape error: You may only add matrices of the same dimensions\n{self.get_shape()}{other.get_shape()}"
            )
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self[(i, j)] += other[(i, j)]
            return self

    def __sub__(self, other):
        if self.shape != other.shape:
            print(
                f"Shape error: You may only subtract matrices of the same dimensons\n{self.get_shape()}{other.get_shape()}"
            )
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self[(i, j)] -= other[(i, j)]
            return self

    def __mul__(self, other):
        # Scalar multiplication
        if (
            type(other) is not Matrix
        ):  # If its just a scalar value, convert it to a 1x1 matrix type of that value
            other = Matrix(1, 1, other)
        if other.shape == (1, 1):
            for i in range(self.rows):
                for j in range(self.cols):
                    self[(i, j)] *= other[(0, 0)]
            return self
        # Matrix Multiplication
        elif self.cols == other.rows:
            result = Matrix(other.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        result[(i, j)] += self[(i, k)] * other[(k, j)]
            return result
        elif self.shape != other.shape:
            print(
                f"Shape error: You may only multiply matrices of the same dimensons\n{self.get_shape()}{other.get_shape()}"
            )

    def __pow__(self, power):
        for i in range(self.rows):
            for j in range(self.cols):
                self[(i, j)] **= power
        return self

    def get_shape(self):
        return f"\nShape:{self.shape}"
