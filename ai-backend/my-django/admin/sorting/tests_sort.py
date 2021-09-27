import unittest
from admin.sorting.models_sort import Sorting


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_arr = [9, 8, 7, 6, 5, 3, 2, 4, 1]
        arr = instance.bubble_sort()
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_merge_sort(self):
        param = [9, 8, 7, 6, 5, 3, 2, 4, 1]
        arr1 = Sorting.merge_sort(param)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(f'result : {arr1}')

    def test_quick_sort(self):
        param = [9, 8, 7, 6, 5, 3, 2, 4, 1]
        arr1 = Sorting.quick_sort(param)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        arr = [99, 8, 17, 6, 51, 3, 21, 4, 1, 2, 5, 9]
        arr2 = Sorting.quick_sort(arr)
        print(arr2)

    def test_hummm(self):
        instance = Sorting()
        instance.var_list = [1,3,5,7]
        arr = instance.hummm()
        print(arr)
        self.assertEqual(arr,1)


if __name__ == '__main__':
    unittest.main()
