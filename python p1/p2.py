import numpy as np
with open ('kiwidata.txt') as file:
    dataset = file.read()

datameme = dataset.split(',')
datameme.remove('')
data = np.array(datameme).astype(np.float64) 


def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(low, high, array):
  if low < high:

    pi = partition(array, low, high)
    quickSort( low, pi - 1,array)
    quickSort( pi + 1, high,array)
  return array

size = len(data)



print('Sorted Array:')
print(quickSort(0,len(datameme)-1,np.copy(datameme)))
