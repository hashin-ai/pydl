from pydl import Matrix

if __name__ == "__main__":
    A = Matrix(2, 2, 2)
    B = Matrix(2, 2, 9)
    C = Matrix(1, 1, 5)

    print("-" * 15)
    print("MATRIX TESTING")
    print(f"A:\n{A}")
    print(f"B:\n{B}")
    print(f"C:\n{C}")

    I = Matrix(10, 10, "i")
    print(f"Identity Matrix:\n{I}\n")

    R = Matrix(4, 4, "r")
    print(f"Random Matrix:\n{R}\n")

    print("-" * 15)

    print(C.shape)

    print(f"A + B\n{A + B}\n")
    print(f"A - B\n{A - B}\n")
    print(f"A * B\n{A * B}\n")
    print(f"A * C\n{A * C}\n")

    print(f"A **2\n{A ** 2}\n")
