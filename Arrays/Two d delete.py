import numpy as np

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_d_array)

newarr=np.delete(two_d_array, 0, axis=0)
print(newarr)

newarr1=np.delete(two_d_array, 0, axis=1)
print(newarr1)

#Time complexity: O(n^2)/O(m*n)
#Space complexity: O(1)