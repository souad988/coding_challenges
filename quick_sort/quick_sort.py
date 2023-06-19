def quick_sort(arr,left,right):
    if left < right:
        pivot_index = partition(arr, left, right)
        #perform sort in left and right sides of pivot index in arr
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index, right)

def partition(arr, left, right):
    pivot_index = left
    pivot = arr[right]

    for i in range(left, right):
        if(arr[i] <= pivot):
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1


    #put pivot in it's index before exit and return pivot_index
    arr[pivot_index] , arr[right] = arr[right], arr[pivot_index]
    return pivot_index

print(quick_sort([7,2,9,1,6,5],0,5))


import numpy as np
import numpy.testing as np_testing
import unittest

class ArrayEqualTest(unittest.TestCase):
    def test_array_equal(self):
        arr1 = np.array([7,2,9,1,6,5])
        quick_sort([7,2,9,1,6,5],0,5)
        arr2 = np.array([1,2,5,6,7,9])
        print(arr1, arr2)
        np_testing.assert_array_equal(arr1, arr2)

if __name__ == '__main__':
    unittest.main()