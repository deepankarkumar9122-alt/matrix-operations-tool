# ==========================================================
# Task 3: Matrix Operations Tool
# Author: Shivans Sharma
# Description:
# A menu-driven Matrix Operations Tool using NumPy.
# ==========================================================

import numpy as np

# ----------------------------------------------------------
# Function to Input Matrix
# ----------------------------------------------------------
def input_matrix(name):
    print(f"\nEnter details for Matrix {name}")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print(f"Enter elements of Matrix {name} row-wise:")

    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != cols:
                    print(f"Incorrect number of elements. Please enter {cols} elements.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

        matrix.append(row)

    return np.array(matrix)

# ----------------------------------------------------------
# Main Program
# ----------------------------------------------------------

print("=" * 60)
print(" MATRIX OPERATIONS TOOL USING NUMPY ")
print("=" * 60)

A = input_matrix("A")
B = input_matrix("B")

while True:

    print("\n")
    print("=" * 60)
    print("Select Matrix Operation")
    print("=" * 60)

    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Transpose of Matrix B")
    print("6. Determinant of Matrix A")
    print("7. Determinant of Matrix B")
    print("8. Display Matrices")
    print("9. Exit")

    choice = input("\nEnter your choice (1-9): ")

    try:

        if choice == "1":

            if A.shape == B.shape:
                print("\nResult:")
                print(A + B)
            else:
                print("\nAddition not possible.")
                print("Matrices must have the same dimensions.")

        elif choice == "2":

            if A.shape == B.shape:
                print("\nResult:")
                print(A - B)
            else:
                print("\nSubtraction not possible.")
                print("Matrices must have the same dimensions.")

        elif choice == "3":

            if A.shape[1] == B.shape[0]:
                print("\nResult:")
                print(np.matmul(A, B))
            else:
                print("\nMultiplication not possible.")
                print("Columns of Matrix A must equal rows of Matrix B.")

        elif choice == "4":

            print("\nTranspose of Matrix A")
            print(A.T)

        elif choice == "5":

            print("\nTranspose of Matrix B")
            print(B.T)

        elif choice == "6":

            if A.shape[0] == A.shape[1]:
                print("\nDeterminant of Matrix A")
                print(np.linalg.det(A))
            else:
                print("\nDeterminant can only be calculated for square matrices.")

        elif choice == "7":

            if B.shape[0] == B.shape[1]:
                print("\nDeterminant of Matrix B")
                print(np.linalg.det(B))
            else:
                print("\nDeterminant can only be calculated for square matrices.")

        elif choice == "8":

            print("\nMatrix A")
            print(A)

            print("\nMatrix B")
            print(B)

        elif choice == "9":

            print("\nThank you for using Matrix Operations Tool!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")

    except Exception as e:
        print("\nError:", e)