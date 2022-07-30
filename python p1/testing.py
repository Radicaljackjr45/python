from os import stat
from tracemalloc import start
from p3 import selectionSort,array
import numpy as np
import time

averageCase=array
bestCase=np.sort(np.copy(array))
worstCase=np.array(bestCase)[::-1]

def test_WorstCaseSelection():
    start= time.time()
    assert np.array_equal(selectionSort(np.copy(worstCase),len(worstCase)),bestCase)
    print(time.time()-start)

def test_BestCaseSelection():
    start= time.time()
    assert np.array_equal(selectionSort(np.copy(bestCase),len(bestCase)),bestCase)
    print(time.time()-start)


def test_AverageCaseSelection():
    start= time.time()
    assert np.array_equal(selectionSort(np.copy(averageCase),len(averageCase)),bestCase)
    print(time.time()-start)
