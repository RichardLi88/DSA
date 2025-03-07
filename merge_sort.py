from typing import List

def merge_sort(unsorted_list: List[int],left,mid,right):
    


def merge(list1: List[int], list2: List[int]):
    new_list = []

    p1,p2 = 0,0

    while p1 < len(list1) and p2 < len(list2):
        if p1 <= p2:
            new_list.append(list1[p1])
            p1 += 1
        else:
            new_list.append(list2[p2]))
            p2 += 1 

    while p1 < len(list1):
        new_list.append(list1[p1])
        p1 +=1 
    
    while p2 < len(list2):
        new_list.append(list2[p2])
        p2 += 1 
    return new_list
