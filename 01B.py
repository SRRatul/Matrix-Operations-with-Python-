# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:04:10 2024

@author:Salvir Rahman Ratul

Add two 2x2 matrices.(take input from user)
"""
import numpy as np
def give_input(name):
    print(f"Enter values for {name}- matrix :")
    matrix = []
    for i in range(2):
        row = input(f"Enter the value for {i + 1}th row (space-separated): ").split()
        matrix.append([int(num) for num in row])
    return np.array(matrix)

matrix_a = give_input('A')
matrix_b = give_input('B')
result = matrix_a + matrix_b
print("Result : ", result)
 