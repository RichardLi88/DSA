from typing import List


def insertion_sort(unsorted_list: List[int]) -> None:
    for i in range(1, len(unsorted_list)):
        for j in range(i, 0, -1):
            if unsorted_list[j] > unsorted_list[j - 1]:
                break
            else:
                unsorted_list[j], unsorted_list[j - 1] = (
                    unsorted_list[j - 1],
                    unsorted_list[j],
                )


random_list = [5, 4, 3, 2, 1]
insertion_sort(random_list)
print(random_list)
