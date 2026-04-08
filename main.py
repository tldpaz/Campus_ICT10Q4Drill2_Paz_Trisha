# a module is a single file containing python code.
# defines: functions, classes, and variables.
# allows code reusability and organization by logically grouping related code together
# u can import modules into other python scripts using the import statement.
# module is like teacher, math.py for math tasks
# from
# - go inside and get smth specific (instead of whole module, u only take what u need)

# PYTHON PACKAGES
# - collection of modules organized in directories
# blablabla
# department groups teachers of related subjects
# in python, package is a fold that contains multiple modules :3 
# Numpty
# + = is one of the most powerful combos in python peak 
#Matplotlib

# from math import sqrt

# print(pow(2,3))

# as - rename for convenience (give it shorter or easier name)

#NumPy - numerical pythonn, important for working with numbers
# written in c
# uses less memory
# supports powerful operators
# used for a lot of stuff 

 #a = np.array([1,2,3])
 #v = np.array([1,2], [3,4])
 #c = np.array([[[1,2], [3,4]]])

 # print(a)
 # print(v)
 # print(c)

 # print(a + v)

 # d = [1,2,3]
 # e = [5,6,7]

 # print(d + e)
 
import numpy as np
import matplotlib.pyplot as plt
from pyscript import display

import numpy as np
import matplotlib.pyplot as plt
from pyscript import display

def sample_numpy(event):
    a = np.array([5, 6, 7])
    b = np.array([8, 9, 10])

    display(a + b, target="output")
    display(a * b, target="output")
    display(a ** b, target="output")

    plt.plot([1, 2, 3], [1, 4, 9])
    plt.savefig("test_plot.png")