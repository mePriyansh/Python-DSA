#Array module
import array

#Array without integers
my_array=array.array('i')
print(my_array)
#Array with integers
my_array1=array.array('i',[1,2,3,4,5])
print(my_array1)

import numpy as np

#Array initialization
np_array=np.array([],dtype=int)
print(np_array)
#Array with integers
np_array1=np.array([1,2,3,4,5])
print(np_array1)