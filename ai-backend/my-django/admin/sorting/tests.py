from django.test import TestCase
import unittest
# import sys
# sys.path.append('/admin/sorting')
from admin.sorting.models import MySum, Palindrome
# from models import MySum (setup)

class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_2()
        print(res)
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

class TestPalindrome(unittest.TestCase):

    def test_isPalindrome(self):
        instance = Palindrome()
        instance.input_string = "appLElppaa"
        res1 = instance.str_to_list()
        res = instance.isPalindrome()
        print(res1)
        print(res)
        res2 = instance.reverse_string()
        print(res2)

if __name__ == '__main__':
    unittest.main()