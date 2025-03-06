from typing import List


def bubble_sort(unsorted_list: List[int]) -> None:
    for i in range(len(unsorted_list) - 1):
        needs_sort = False
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                needs_sort = True
                unsorted_list[j], unsorted_list[j + 1] = (
                    unsorted_list[j + 1],
                    unsorted_list[j],
                )
        if needs_sort == False:
            break


random_list = [5, 4, 3, 2, 1]
bubble_sort(random_list)
print(random_list)
