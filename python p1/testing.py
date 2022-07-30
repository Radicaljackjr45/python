from p3 import selectionSort,array
import numpy as np

averageCase=array
bestCase=np.sort(np.copy(array))
worstCase=np.array(bestCase)[::-1]

def test_WorstCaseSelection():
    assert np.array_equal(selectionSort(np.copy(worstCase),len(worstCase)),bestCase)

def test_BestCaseSelection():
    assert np.array_equal(selectionSort(np.copy(bestCase),len(bestCase)),bestCase)

def test_AverageCaseSelection():
    assert np.array_equal(selectionSort(np.copy(averageCase),len(averageCase)),bestCase)