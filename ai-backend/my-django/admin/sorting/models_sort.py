from dataclasses import dataclass
# Create your models here.
# from django.db import models

@dataclass
class Sorting(object):

    random_arr :[]
    var_list : []

    @property
    def var_list(self) -> [] :return self._var_list

    @var_list.setter
    def var_list(self, var_list): self._var_list = var_list

    @property
    def random_arr(self) -> []: return self._random_arr

    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self):
        arr = self.random_arr
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

        # for i in range(1, len(A)):
        #     for j in range(0, len(A)-1):
        #         if A[j] > A[j+1]:
        #             A[j], A[j+1] = A[j+1], A[j]

    @staticmethod
    def merge_sort(param:[]):
        arr = param
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        arr1 = Sorting.merge_sort(arr[:mid])
        arr2 = Sorting.merge_sort(arr[mid:])
        arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        arr += arr1[i:]
        arr += arr2[j:]
        return arr

        # if len(arr) < 2:
        #     return arr
        # mid = len(arr)//2
        # low_arr = merge_sort(arr[:mid])
        # high_arr = merge_sort(arr[mid:])
        # merged_arr = []
        # l = h = 0
        # while l < len(low_arr) and h < len(high_arr):
        #     if low_arr[l] < high_arr[h]:
        #         merged_arr.append(low_arr[l])
        #         l += 1
        #     else:
        #         merged_arr.append(high_arr[h])
        #         h += 1
        # merged_arr += low_arr[l:]
        # merged_arr += high_arr[h:]
        # print(merged_arr)
        # return merged_arr

    @staticmethod
    def quick_sort(param:[]):
        arr = param
        if len(arr) <= 1:
            return arr
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [], [], []
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        # print(arr1, arr2, arr3)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)


    def hummm(self):
        arr = self.var_list
        str = ""
        str2 =[]
        for i in arr:
            print(i)
            str += f'{i}'
            str2 += f'{i}'
            # str.append(i)
        return str , str2