class Matrix:
    def __init__(self, rows, cols, default_values):
        self.rows = rows
        self.cols = cols
        self.shape = (rows, cols)
        if default_values == 'random':
            pass  # Generate a matrix of random values
        elif default_values == "eye":
            pass # Generate identity matrix
        else:
            self.values = [[default_values]*cols for val in range(rows)]

    def __str__(self):
        return '\n'.join(map(str, [value for value in self.values]))

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
                f"Shape error: You may only add matrices of the same dimensions\n{self.get_shape()}{other.get_shape()}")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self[(i, j)] += other[(i, j)]
            return self

    def __sub__(self, other):
        if self.shape != other.shape:
            print(
                f"Shape error: You may only subtract matrices of the same dimensons\n{self.get_shape()}{other.get_shape()}")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self[(i, j)] -= other[(i, j)]
            return self

    def __mul__(self, other):
        # Scalar multiplication
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
                f"Shape error: You may only multiply matrices of the same dimensons\n{self.get_shape()}{other.get_shape()}")

    def get_shape(self):
        return (f"\nShape:{self.shape}")


if __name__ == "__main__":
    print("-" * 15)
    print("MATRIX TESTING")
    print("-" * 15)

    A = Matrix(2, 2, 2)
    B = Matrix(2, 2, 9)
    C = Matrix(1, 1, 5)

    print(C.shape)

    print(f"A + B\n{A + B}\n")
    print(f"A - B\n{A - B}\n")
    print(f"A * B\n{A * B}\n")
    print(F"A * C\n{A * C}\n")
