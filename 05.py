# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:22:44 2024

@author: Salvir Rahman Ratul
Create amatrix with random integers.
"""

import numpy as np
rand_mat = np.random.randint(10, 20, size=(3,4))
stored_mat = rand_mat #storing the random matrix
print(rand_mat)
rand_mat = rand_mat + np.random.randint(20, 80, size=(3,4))
print(rand_mat)
x_mat = rand_mat - stored_mat #finding the random matrix which is added to the old matrix
print(x_mat)