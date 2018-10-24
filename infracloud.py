import pandas as pd
import numpy as np
from itertools import product, starmap

#creating matrix
r = 4
normal_matrix = np.random.rand(r,r)
print(normal_matrix)


#Finding adjacent position
x, y = (1, 1)
cells = starmap(lambda a,b: (x+a, y+b), product((0,-1,+1), (0,-1,+1)))
r = list(cells)
print(r)
print(normal_matrix[1,1])

#Finding adjacent position
x,y=(2,2)
cells = starmap(lambda a,b: (x+a, y+b), product((0,-1,+1,+2), (0,-1,+1,+2)))
r = list(cells)
print(r)