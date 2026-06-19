#np.nan_to_nan is used to replace the missing values with np.nan

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])
clean_arr = np.nan_to_num(arr, nan=0)
print(clean_arr)    

