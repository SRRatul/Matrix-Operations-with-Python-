# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:00:22 2024

@author: Salvir Rahman Ratul
Ones Matrix
"""

import numpy as np
ones_matrix = np.ones((2,2))
print(ones_matrix)
ones_matrix = np.ones((4,3))
print(ones_matrix)
ones_matrix = np.ones((3,4)) + np.ones((3,4))
print(ones_matrix)
for i in range(3):
    ones_matrix = ones_matrix + np.ones((3,4))
print(ones_matrix)