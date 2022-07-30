import numpy as np
with open ('kiwidata.txt') as file:
    dataset = file.read()

dataString = dataset.split(',')
dataString.remove('')
data = np.array(dataString).astype(np.float64)   


def bubble(list_1):
    indexing_length = len(list_1) - 1
    sorted = False



    while not sorted:
        sorted = True
        for a in range(0, indexing_length):
            if list_1[a] > list_1[a+1]:
                sorted = False 
                list_1[a], list_1[a+1] = list_1[a+1], list_1[a]
    return list_1
print('Sorted Array:')
print(bubble(data))