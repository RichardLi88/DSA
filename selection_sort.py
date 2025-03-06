import math
from typing import List


def selection_sort(unsorted_list: List[int]):
    for i in range(len(unsorted_list) - 1):
        cur_min = math.inf
        index = None
        for j in range(i, len(unsorted_list)):
            if unsorted_list[j] < cur_min:
                cur_min = unsorted_list[j]
                index = j
        unsorted_list[i], unsorted_list[index] = unsorted_list[index], unsorted_list[i]


random_list = [5, 4, 3, 2, 1]
selection_sort(random_list)
print(random_list)
