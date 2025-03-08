from typing import List


def merge_sort(unsorted_list: List[int], left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(unsorted_list, left, mid)
        merge_sort(unsorted_list, mid + 1, right)
        merge(unsorted_list, left, mid, right)


def merge(unsorted_list, start, mid, end):
    start2 = mid + 1
    if unsorted_list[start2] >= unsorted_list[mid]:
        return

    while start <= mid and start2 <= end:
        if unsorted_list[start] <= unsorted_list[start2]:
            start += 1
        else:
            current, value = start2, unsorted_list[start2]

            while current != start:
                unsorted_list[current] = unsorted_list[current - 1]
                current -= 1

            unsorted_list[start] = value

            start += 1
            start2 += 1
            mid += 1
        print(unsorted_list)


if __name__ == "__main__":
    unsorted_list = [5, 4, 3, 2, 1]
    merge_sort(unsorted_list, 0, len(unsorted_list) - 1)
    print(unsorted_list)
