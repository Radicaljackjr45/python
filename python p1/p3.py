import numpy as np
import time

array = np.loadtxt(fname='C:\\Users\\punfu\\python p1\\kiwidata.txt',delimiter=",")
 
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    return array



print('Sorted Array:')
print(selectionSort(array,len(array)))