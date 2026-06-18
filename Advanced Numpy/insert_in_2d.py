import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)

#insert a new row ar index 1
new_arr = np.insert(arr_2d,1,[10,20,30,],axis=0)
print(new_arr)
