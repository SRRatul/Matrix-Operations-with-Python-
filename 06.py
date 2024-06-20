# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:35:01 2024

@author:Salvir Rahman Ratul
Create diagonal matrix with specific values on the diagonal.
"""

import numpy as np 
diagonal = [1, 2, 3, 4, 5]
diag_matrix = np.diag(diagonal)
print(diag_matrix)
#Extra practice
dia_value = [3, 4, 5]
dia_mat = np.diag(dia_value) + np.eye(3) + np.ones(3)+ np.random.randint(0, 5, size=(3)) + np.zeros(3)
print(dia_mat)