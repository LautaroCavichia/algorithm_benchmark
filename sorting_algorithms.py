import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst


def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst.pop()
    left = [x for x in lst if x <= pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def randomized_quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst.pop(random.randint(0, len(lst)-1))
    left = [x for x in lst if x <= pivot]
    right = [x for x in lst if x > pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged

